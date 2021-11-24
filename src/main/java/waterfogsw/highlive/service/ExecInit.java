package waterfogsw.highlive.service;

import java.util.ArrayList;
import java.util.List;

public class ExecInit implements ExecPython{
    private String videoId;
    private final String initPath = "./python/init.py";

    public ExecInit(String videoId) {
        this.videoId = videoId;
    }

    @Override
    public void run() {
        List<String> command = new ArrayList<>();

        command.add("python3");
        command.add(initPath);
        command.add(videoId);

        ProcessRunner.run(command);
    }
}
