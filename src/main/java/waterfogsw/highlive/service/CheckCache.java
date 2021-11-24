package waterfogsw.highlive.service;

import java.io.File;

public class CheckCache {
    private static String cachePath = "./python/Data/traffic_data/";
    public static boolean checkByVideoId(String videoId){

        File f = new File(cachePath+videoId+".json");
        return f.exists();
    }
}
