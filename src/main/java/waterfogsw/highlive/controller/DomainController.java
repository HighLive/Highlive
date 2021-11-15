package waterfogsw.highlive.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;


import javax.servlet.http.HttpServletRequest;

@Controller
public class DomainController {
    @GetMapping("/")
    public String index() {
        return "dashboard";
    }

    @ResponseBody
    @PostMapping("/analyze")
    public String analyze(HttpServletRequest request) {
        String temp = request.getParameter("url") + '\n';

        try {
            temp = temp.substring(temp.length() - 11);
        } catch(IndexOutOfBoundsException e) {
            return "Invalid Index";
        }
        return temp;
    }

}
