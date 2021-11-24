import json, datetime, sys, os

import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

IMOTION_NUM = 5

def classify_emotion(json_data):
    emotion_count = 0
    emotion_score = {'joy': 0, 'fear': 0, 'sadness': 0, 'disgust': 0, 'anger': 0}
    valid_score = {'valid': 0, 'invalid': 0}

    # 추후 단어 추가
    # [ [joy 식별단어], [fear .. ], [sadness .. ], [disgust .. ], [anger ..] ]
    emotion_words = [
        ["joy", "웃기네", "웃기다", "웃김", "ㅋㅋㅋ", "ㅎㅎㅎ"],
        ["fear", "..", "무섭네", "무섭다", "소름", "ㄷㄷ"],
        ["sadness", "슬프다", "ㅠㅠ", "감동", "슬프네"],
        ["disgust", "역겹네", "역겹다", "우웩", "윽", "혐오"],
        ["anger", "빡치네", "빡침", "열받네", "화나", "킹받"]
    ]

    for chat in json_data:
        chatData = json_data[chat]['content']
        validFlag = True

        # 특정 문자를 기준으로 scoring
        chatList = list(json_data[chat]['content'])
        mainChar = max(set(chatList), key=chatList.count)

        if (mainChar == "ㅋ"):
            emotion_score['joy'] += 1
            emotion_count += 1
        elif (mainChar == "ㄷ"):
            emotion_score['fear'] += 1
            emotion_count += 1
        elif (mainChar == "ㅠ"):
            emotion_score['sadness'] += 1
            emotion_count += 1
        elif (mainChar == "ㅡ"):
            emotion_score['disgust'] += 1
            emotion_count += 1
        elif (mainChar == "ㅗ"):
            emotion_score['anger'] += 1
            emotion_count += 1
        else:
            validFlag = False

        # 특정 단어를 기준으로 scoring
        for words in emotion_words:
            emotion = words[0]
            for word in words:
                if word in chatData:
                    emotion_score[emotion] += 1
                    validFlag = True
                    emotion_count += 1

        if validFlag:
            valid_score['valid'] += 1
        else:
            valid_score['invalid'] += 1

    emotion_score['joy'] = round(emotion_score['joy'] / emotion_count * 100.0, 1)
    emotion_score['fear'] = round(emotion_score['fear'] / emotion_count * 100.0, 1)
    emotion_score['sadness'] = round(emotion_score['sadness'] / emotion_count * 100.0, 1)
    emotion_score['disgust'] = round(emotion_score['disgust'] / emotion_count * 100.0, 1)
    emotion_score['anger'] = round(emotion_score['anger'] / emotion_count * 100.0, 1)

    valid_data_cnt = valid_score['valid']
    invalid_data_cnt = valid_score['invalid']
    valid_score['valid'] = round((valid_data_cnt / (valid_data_cnt+invalid_data_cnt)) * 100.0, 1)
    valid_score['invalid'] = round((invalid_data_cnt / (valid_data_cnt+invalid_data_cnt)) * 100.0, 1)


    return  emotion_score, valid_score

def return_json(result_data, result_path):
    temp = result_data
    result_json = [[k, v] for k, v in temp.items()]
    with open(result_path, 'w') as outfile:
        json.dump(result_json, outfile)


# MAIN
def main(argv):

    video_id = argv[1]

    # java process builder를 통해 실행시킬 경우 다음의 경로를 따라야 함
    raw_path = "./python/Data/raw_data/" + video_id + ".json"
    emotion_path = "./python/Data/emotion_data/" + video_id + ".json"
    valid_path = "./python/Data/valid_data/" + video_id + ".json"

    with open(raw_path, encoding='UTF-8') as jFile:
        json_data = json.load(jFile)

    # 채팅 데이터에서 각 시간별 채팅 빈도수만 뽑아서 반환
    classify_emotion((json_data))
    emotion_class, valid_class = classify_emotion(json_data)

    print(emotion_class)
    print(valid_class)

    # 감정 점수 결과 JSON 반환
    return_json(emotion_class, emotion_path)
    # 유효 점수 결과 JSON 변환
    return_json(valid_class, valid_path)


if __name__ == "__main__":
    main(sys.argv)
