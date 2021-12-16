import json
import sys
import os
from path import Path

def secToTime(sec):
    _hour = sec // (60*60)
    sec = sec - _hour*(60*60)
    _min = sec // 60
    sec = sec - _min*(60)

    if int(_hour / 10) == 0:
        _hour = "0" + str(_hour)
    else:
        _hour = str(_hour)

    if int(_min / 10) == 0:
        _min = "0" + str(_min)
    else:
        _min = str(_min)
   
    if int(sec / 10) == 0:
        sec = "0" + str(sec)
    else:
        sec = str(sec)
    return _hour + ":" + _min + ":" + sec
   
def write_data_for_ffmpeg(start_time, time, path):
    with open(path, 'a') as outfile:
        data = start_time + "-" + time + "\n"
        outfile.write(data)



# 동영상 mkv 파일 다운로드
def main(argv):
    video_id = argv[1]
    highlight_path = Path.highlight.value+video_id+".json"
    preprocess_path = Path.preprocess.value+video_id+".txt"
    video_dir_path = Path.videos.value

    if os.path.isfile(preprocess_path):
        return

    with open(highlight_path, encoding='UTF-8') as jFile:
        json_data = json.load(jFile)

    # write process_data
    for section in json_data:
        start_time = secToTime(section[0])
        time = secToTime(section[1] - section[0])
        write_data_for_ffmpeg(start_time, time, preprocess_path)

    # 쉘 스크립트 동작
    #os.system('ls')
    #command = 'echo ' + video_dir_path
    os.system('echo check@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    comd = video_dir_path + 'edit.sh' + ' ' + video_id + ' ' + video_dir_path + ' ' + preprocess_path
    os.system(comd)
    #os.system(video_dir_path + 'edit.sh' + video_id + ' ' + video_dir_path)
    

   


if __name__ == "__main__":
    main(sys.argv)