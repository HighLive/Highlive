package waterfogsw.highlive.service;

import java.util.ArrayList;
import java.util.List;

public class ExecClassifyEmotion implements ExecPython{
    private String videoId;
    private final String emotionPath = "./python/emotion.py";

    public ExecClassifyEmotion(String videoId) {
        this.videoId = videoId;
    }

    @Override
    public void run() {
        List<String> command = new ArrayList<>();

        command.add("python3");
        command.add(emotionPath);
        command.add(videoId);

        ProcessRunner.run(command);
    }
}
