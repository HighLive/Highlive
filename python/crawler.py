import requests
import json
from collections import OrderedDict


def getChatLog(video_id: str, client_id: str) -> list:
    next_cursor = ""
    params = {}
    params['client_id'] = client_id

    chat_log = []
    log_cnt = 0

    # 한번의 Get요청에 약 57 ~ 59개의 comment에 대한 json파일을 load한다
    # next_cursor는 다음 채팅데이터를 가리키고 있음
    while True:
        URL = "https://api.twitch.tv/v5/videos/" + \
              video_id + "/comments?cursor=" + next_cursor

        response = requests.get(URL, params=params)
        chat_json = json.loads(response.text)
        chat_log.append(chat_json['comments'])

        try:
            next_cursor = chat_json["_next"]
            log_cnt += 1
        except KeyError:
            break
    return chat_log


# 로그(list)를 받아 json형식(dict)으로 변환
def LogToJson(log):
    index = 0
    result = OrderedDict()
    for l in log:
        for comment in l:
            msg = OrderedDict()
            index += 1

            msg['time'] = comment["content_offset_seconds"]
            msg['user_id'] = comment['commenter']['_id']
            msg['content'] = comment['message']['body']

            result["message" + str(index)] = msg
    return result