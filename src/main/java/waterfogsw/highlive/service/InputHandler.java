package waterfogsw.highlive.service;

public class InputHandler {
    private String url;
    private String video_id;

    private static final String pathOfCrawler = "../pythonProgram";
    private static final String pathOfFindHighligh = "../pythonProgram";

    private static final ExecCrawler execCrawler = new ExecCrawler(pathOfCrawler);
//    private static final ExecFindHighlight execFH = new ExecFindHighlight(pathOfFindHighlight);
}
