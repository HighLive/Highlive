package waterfogsw.highlive.service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class ExecExtractVideo implements ExecPython {
    private String videoId;
    private final String videoPath = "./python/video.py";

    public ExecExtractVideo(String videoId) {
        this.videoId = videoId;
    }

    @Override
    public void run() {
        List<String> command = new ArrayList<>();
	
        System.out.println("exec video.py");

        command.add("python3");
        command.add(videoPath);
        command.add(videoId);

        ProcessRunner.run(command);
    }
}
