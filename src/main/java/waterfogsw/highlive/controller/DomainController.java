package waterfogsw.highlive.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import waterfogsw.highlive.service.InputHandler;


import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

@Controller
public class DomainController {
    private final InputHandler inputHandler;

    @Autowired
    public DomainController(InputHandler inputHandler) {
        this.inputHandler = inputHandler;
    }

    @GetMapping("/")
    public String index() {
        return "index";
    }

    @PostMapping("/result")
    public String result(HttpServletRequest request, Model model) {
        String url = request.getParameter("url");
        StringTokenizer st = new StringTokenizer(url, "/");
        String video_id = "";

        List<String> pstr = new ArrayList<>();
        while(st.hasMoreTokens()) {
            pstr.add(st.nextToken());
        }

        boolean validCheck = false;
        try {
            for(int i=0; i<pstr.size(); i++){
                if(pstr.get(i).equals("videos")) {
                    video_id = pstr.get(i+1);
                    validCheck = true;
                    break;
                }
            }
        } catch(IndexOutOfBoundsException e) {
            return "invalid_videoId";
        }

        if(!validCheck){
            return "404";
        }

        // 크롤링
        inputHandler.runCrawler(video_id);

        // 감정분석
        inputHandler.runClassifyEmotion(video_id);

        // 트래픽 추출
        inputHandler.runFindHighlight(video_id);

        model.addAttribute("videoId", video_id);

        return "result";
    }

}