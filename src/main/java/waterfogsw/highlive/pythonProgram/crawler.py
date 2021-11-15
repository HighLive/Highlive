import sys
import requests
import json

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

        ##
        #print(chat_json['comments'])
        ##
        
        try:
            next_cursor = chat_json["_next"]
            log_cnt += 1
        except KeyError:
            break

        #print(chat_log.)
    return chat_log


from collections import OrderedDict

# list(Json) 객체를 받아 ./temp.json 으로 저장
def LogToJson(video_id, log):
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

    ### for local
    # path = "C:/Users/jinh2/Desktop/2021-2/capstone/DreamChat_Demo_01/DreamChat_Demo_01/src/main/resources/static/json/"
    
    ### for ubuntu
    # path = "/home/ubuntu/highlive/DreamChat_Demo_01/DreamChat_Demo_01/src/main/resources/static/json/"
    
    fileName = "./Data/" + video_id + ".json"    

    with open(fileName, 'w', encoding='utf8') as outfile:
        json.dump(result, outfile, indent = 4, ensure_ascii=False)
    return


# MAIN

def main(argv):
    print("START MAIN")
    
    video_id = argv[1]
    #print(video_id)
    #print(type(video_id))
    #video_id = "724229279"
    
    #video_id = argv[1]
    
    # print("type------------------")
    # print(type(video_id))
    # print(video_id)
    
    log = getChatLog(video_id, "f0tc0p4p3mifcdxtwi530swm2dsw0f")
    LogToJson(video_id, log)
    
    print("END MAIN")
    
    find_highilght

if __name__ == "__main__":
    main(sys.argv)