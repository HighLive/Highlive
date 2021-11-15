package waterfogsw.highlive;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class ExecApp {

    private static final String crawlerPath = "./src/main/java/waterfogsw/highlive/pythonProgram/crawler.py";

    public static void main(String[] args) throws IOException, InterruptedException {
        List<String> command = new ArrayList<>();
        command.add("python3");
        command.add(crawlerPath);
        command.add("1167834289");

        // Exec Crawler
        ProcessBuilder processBuilder = new ProcessBuilder(command);
        Process process = processBuilder.start();

        process.waitFor();

        InputStream psout = process.getInputStream();
        BufferedReader br = new BufferedReader(new InputStreamReader(psout));

        String line;
        StringBuilder output = new StringBuilder();
        while ((line = br.readLine()) != null) {
            output.append(line);
        }
        br.close();

        System.out.println(output.toString());
    }
}
