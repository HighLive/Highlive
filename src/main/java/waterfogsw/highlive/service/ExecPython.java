package waterfogsw.highlive.service;

import java.io.IOException;

public interface ExecPython {
    int execPythonProgram(String arg);
    int execByCommandLine(String[] command) throws IOException, InterruptedException;
}
