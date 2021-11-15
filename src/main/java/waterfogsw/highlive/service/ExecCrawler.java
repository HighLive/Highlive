package waterfogsw.highlive.service;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ExecCrawler implements ExecPython {

    private String path;

    public ExecCrawler(String path) {
        this.path = path;
    }

    @Override
    public int execPythonProgram(String arg) {
        String[] commands = new String[3];
        commands[0] = "python3";
        commands[1] = path + "/crawler.py"; // 파이썬 실행 프로그램 경로
        commands[2] = arg;      // vedio_id
        int result = -1;

        // 커멘드라인으로 파이썬 프로그램 실행
        try {
            result = execByCommandLine(commands);
        } catch (Exception e) {
            e.printStackTrace();
            return 1;
        }

        return result;
    }

    @Override
    public int execByCommandLine(String[] command) throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder(command[0], command[1], command[2]);
        Process process = processBuilder.start();

        int exitVal = process.waitFor();

        BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream(), "euc-kr")); // 서브 프로세스가 출력하는 내용을 받기 위해
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(">>>  " + line); // 표준출력에 쓴다
        }

        if(exitVal != 0) {
            System.out.println("서브 프로세스가 비정상 종료되었다."); // 비정상 종료
        }

        return 0;   // 정상 수행
    }
}
