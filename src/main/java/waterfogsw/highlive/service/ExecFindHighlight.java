package waterfogsw.highlive.service;

import java.util.ArrayList;
import java.util.List;

public class ExecFindHighlight implements ExecPython{
    private static final String highlightPath = "./python/highlight.py";
    @Override
    public void execPython(String videoId) {
        List<String> command = new ArrayList<>();

        command.add("python3");
        command.add(highlightPath);
        command.add(videoId);

        ProcessRunner.run(command);
    }
}
