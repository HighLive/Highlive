import sys

from myio import make_path, return_json
import crawler
import highlight

from multiprocessing import Process, Manager

def temp(shared_log, shared_path):
    chat_count =  highlight.check_frequency(shared_log)
    moving_avg_data = highlight.data_preprocessing(chat_count)
    highlight_data, leng = highlight.find_highlight(moving_avg_data)
    highlight_data.print_result(highlight_data, leng)

    return_json(moving_avg_data, shared_path['traffic_data'])
    return_json(highlight_data, shared_path['highlight_data'])

# MAIN
def main(argv):
    video_id = argv[1]
    twitch_client_id = "f0tc0p4p3mifcdxtwi530swm2dsw0f"
    manager = Manager()
    procs = []

    # java process builder를 통해 실행시킬 경우 다음의 경로를 따라야 함
    data_dir = "./python/Data/"
    data_type = [
        'raw_data', 
        'traffic_data', 
        'highlight_data',
        'emotion_data',
        'valid_data'
    ]

    shared_path = manager.dict(make_path(data_dir, data_type, video_id))

    print("START MAIN")
    log = crawler.getChatLog(video_id, twitch_client_id)
    shared_log = manager.dict(crawler.LogToJson(log))

    ## toJSON
    proc = Process(target=return_json, args=(shared_log, shared_path['raw_data']))
    proc.start()
    procs.append(proc)
    
    ## Highlight
    proc = Process(target=temp, args=(shared_log, shared_path))
    proc.start()
    procs.append(proc)

    for proc in procs: proc.join()
    print("END MAIN")


if __name__ == "__main__":
    main(sys.argv)
