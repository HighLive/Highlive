package waterfogsw.highlive.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
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

    //    @ResponseBody
//    @PostMapping("/loading")
//    public String analyze(HttpServletRequest request) {
//
//        String token = "/";
//        String temp = request.getParameter("url");
//        StringTokenizer strTk = new StringTokenizer(temp, token);
//        String video_id = "";
//
//        ArrayList<String> pstr = new ArrayList<>();
//        while(strTk.hasMoreTokens()){
//            pstr.add(strTk.nextToken());
//        }
//
//        try {
//            boolean find_Video_id = false;
//            for(int i=0; i<pstr.size(); i++){
//                //System.out.println(pstr.get(i));
//                if(pstr.get(i).equals("videos")) {
//                    find_Video_id = true;
//                    video_id = pstr.get(i+1);
//                    break;
//                }
//            }
//        } catch(IndexOutOfBoundsException e) {
//            return "Invalid Index";
//        }
//
//        return video_id;
//    }
//
    @PostMapping("/result")
    public String result(HttpServletRequest request) {
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

        inputHandler.runCrawler(video_id);
        inputHandler.runFindHighlight(video_id);

        return "result";
    }

}