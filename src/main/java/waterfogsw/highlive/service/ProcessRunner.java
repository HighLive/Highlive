package waterfogsw.highlive.service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class ProcessRunner {
    public static void run(List<String> command) {
        try {
            Process process = new ProcessBuilder(command).start();
            BufferedReader stdOut = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String str;
            while((str = stdOut.readLine()) != null) {
                System.out.println(str);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
