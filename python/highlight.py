import json, sys
import pandas as pd

from path import Path
from functions import return_json
from functions import print_traffic

def check_frequency(json_data):
    n = int(json_data.popitem()[1]['time'])+1
    freq = [0]*n
    for chat in json_data:
        freq[int(json_data[chat]['time'])] += 1
    chat_count = pd.Series(freq)

    return chat_count  # 시간대별 채팅 수 반환


def moving_average(chat_count, WIN=7):
    # WIN: 이동평균 인자 (default: 7)
    moving_avg = chat_count.rolling(WIN).mean()
    moving_avg[range(WIN-1)] = 0

    return moving_avg


def data_preprocessing(moving_avg, START=0):
    # 앞부분 자르기(START)
    moving_avg = moving_avg.drop(range(1,START))

    # 채팅 빈도순으로 정렬
    processed_data = moving_avg.sort_values(ascending=[False])

    return processed_data


def find_highlight(data, TERM=10, LENGTH=60 * 10):
    # TERM: 단편 하이라이트의 최소 길이 (default: 10sec)
    # LENGTH: 전체 하이라이트 길이 (default: 10min)
    H = []
    hileng = 0
    num = 0
    while (hileng < LENGTH and num < len(data)):
        hileng = 0
        peaktime = int(data.index[num])
        H.append([max(peaktime - TERM, 0), peaktime])
        H.sort()
        try:
            for i in range(0, len(H)):
                while (True):
                    if H[i][1] >= H[i + 1][0]:
                        if H[i][1] <= H[i + 1][1]:
                            H[i] = [H[i][0], H[i + 1][1]]
                        del H[i + 1]
                    else: break
        except IndexError:
            for t in H:
                hileng += t[1] - t[0]
        num += 1

    return H, hileng  # 하이라이트 구간, 전체길이 반환


# MAIN
def main(argv):
    video_id = argv[1]
    raw_path = Path.raw.value+video_id+".json"
    traffic_path = Path.traffic.value+video_id+".json"
    highlight_path = Path.highlight.value+video_id+".json"

    with open(raw_path, encoding='UTF-8') as jFile:
        json_data = json.load(jFile)

    # 채팅 빈도수 계산
    chat_count = check_frequency(json_data)

    # 이동평균 적용
    moving_avg = moving_average(chat_count)

    # 채팅 트래픽에 따른 정렬
    preprocessed_data = data_preprocessing(moving_avg)

    # 하이라이트 구간 추출 (leng: 전체 길이)
    highlight, leng = find_highlight(preprocessed_data, LENGTH=len(chat_count)//5)

    # 결과 출력
    print_traffic(highlight, leng)

    # 이동평균 결과 JSON 반환
    traffic_json=[]
    for i,v in moving_avg.items(): traffic_json.append([i,round(v,2)])
    return_json(traffic_json, traffic_path)

    # 하이라이트 결과 JSON 반환
    return_json(highlight, highlight_path)

if __name__ == "__main__":
    main(sys.argv)
