package waterfogsw.highlive.controller;

import org.springframework.web.bind.annotation.*;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

@RestController
public class ApiController {

    static final String dataPath = "./python/Data/";

    @RequestMapping(value = "/api/traffic/{id}", method = RequestMethod.GET)
    public String getTraffic(@PathVariable("id") String videoId) throws IOException {
        File resource = new File(dataPath + "traffic_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }

    @RequestMapping(value = "/api/emotion/{id}", method = RequestMethod.GET)
    public String getEmotion(@PathVariable("id") String videoId) throws IOException {
        File resource = new File(dataPath + "emotion_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }

    @RequestMapping(value = "/api/highlight/{id}", method = RequestMethod.GET)
    public String getHighlight(@PathVariable("id") String videoId) throws IOException {
        File resource = new File(dataPath + "highlight_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }

    @RequestMapping(value = "/api/valid/{id}", method = RequestMethod.GET)
    public String getValid(@PathVariable("id") String videoId) throws IOException {
        File resource = new File(dataPath + "valid_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }

    @RequestMapping(value = "/api/raw/{id}", method = RequestMethod.GET)
    public String getRaw(@PathVariable("id") String videoId) throws IOException {
        File resource = new File(dataPath + "raw_data/"+ videoId + ".json");

        return new String(Files.readAllBytes(resource.toPath()));
    }
}
