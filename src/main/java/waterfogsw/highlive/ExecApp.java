package waterfogsw.highlive;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class ExecApp {

    private static final String crawlerPath = "./python/crawler.py";
    private static final String highlightPath = "./python/highlight.py";

    public static void main(String[] args) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();

        command.add("python3");
        command.add(highlightPath);
        command.add("1204174820");

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
