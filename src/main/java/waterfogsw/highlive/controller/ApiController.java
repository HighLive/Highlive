package waterfogsw.highlive.controller;


import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

@Controller
public class ApiController {
    @ResponseBody
    @RequestMapping(value = "/api/json/{id}", method = RequestMethod.GET)
    public String getJsonFile(@PathVariable("id") String videoId) throws IOException {

        File resource = new File("./python/Data/result_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }
}
