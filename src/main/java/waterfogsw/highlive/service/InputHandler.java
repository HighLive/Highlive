package waterfogsw.highlive.service;

import org.springframework.stereotype.Service;
@Service
public class InputHandler {

    public void runInit(String videoId) {
        ExecInit execInit = new ExecInit(videoId);
        execInit.run();
    }

    public void runCrawler(String videoId) {
        ExecCrawler execCrawler = new ExecCrawler(videoId);
        execCrawler.run();
    }

    public void runFindHighlight(String videoId) {
        ExecFindHighlight execFindHighlight = new ExecFindHighlight(videoId);
        execFindHighlight.run();
    }

    public void runClassifyEmotion(String videiId){
        ExecClassifyEmotion execClassifyEmotion = new ExecClassifyEmotion(videiId);
        execClassifyEmotion.run();
    }
}
