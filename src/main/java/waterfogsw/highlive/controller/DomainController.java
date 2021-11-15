package waterfogsw.highlive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;


import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.StringTokenizer;

@Controller
public class DomainController {
    @GetMapping("/")
    public String index() {
        return "dashboard";
    }

    @ResponseBody
    @PostMapping("/analyze")
    public String analyze(HttpServletRequest request) {

        String token = "/";
        String temp = request.getParameter("url");
        StringTokenizer strTk = new StringTokenizer(temp, token);
        String video_id = "";

        ArrayList<String> pstr = new ArrayList<>();
        while(strTk.hasMoreTokens()){
            pstr.add(strTk.nextToken());
        }

        try {
            boolean find_Video_id = false;
            for(int i=0; i<pstr.size(); i++){
                //System.out.println(pstr.get(i));
                if(pstr.get(i).equals("videos")) {
                    find_Video_id = true;
                    video_id = pstr.get(i+1);
                    break;
                }
            }
        } catch(IndexOutOfBoundsException e) {
            return "Invalid Index";
        }

        return video_id;
    }

}