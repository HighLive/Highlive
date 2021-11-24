package waterfogsw.highlive.controller;

import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

@RestController
public class ApiController {

    @RequestMapping(value = "/api/json/{id}", method = RequestMethod.GET)
    public String getJsonFile(@PathVariable("id") String videoId) throws IOException {

        File resource = new File("./python/Data/result_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }
}
