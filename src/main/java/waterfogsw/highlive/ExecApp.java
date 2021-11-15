package waterfogsw.highlive;

import java.io.*;
import java.util.ArrayList;

public class ExecApp {

    private static final String crawlerPath = "./pythonProgram/crawler.py";

    public void byRuntime(String[] command) {
//        Runtime run;
    }
    private void printStream(Process process) throws IOException, InterruptedException {
        try (InputStream psout = process.getInputStream()) {
            copy(psout, System.out);
        }
    }

    public void copy(InputStream input, OutputStream output) throws IOException {
        byte[] buffer = new byte[1024];
        int n = 0;
        while ((n = input.read(buffer)) != -1) {
            output.write(buffer, 0, n);
        }
    }
}
