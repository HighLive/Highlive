package waterfogsw.highlive.service;

import java.util.ArrayList;
import java.util.List;

public class ExecFindHighlight implements ExecPython{
    private String videoId;
    private final String highlightPath = "./python/highlight.py";

    public ExecFindHighlight(String videoId) {
        this.videoId = videoId;
    }

    @Override
    public void run() {
        List<String> command = new ArrayList<>();

        command.add("python3");
        command.add(highlightPath);
        command.add(videoId);

        ProcessRunner.run(command);
    }
}
