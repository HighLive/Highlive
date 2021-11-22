import json, datetime, sys
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

def check_frequency(json_data):
    timeData=[]
    for chat in json_data:
        timeData.append(int(json_data[chat]['time']))

    freq = Counter(timeData)
    temp = pd.Series(freq)
    chat_count = temp.reindex(list(range(1,temp.last_valid_index()+1)), fill_value=0)

    return chat_count   # 시간대별 채팅 수 반환


# START: 하이라이트 측정 (default: 0)
# WIN: 이동평균 인자 (default: 7)
def data_preprocessing(chat_count, START=0, WIN=7):
    # 이동평균 적용(WIN)
    moving_avg = chat_count.rolling(WIN).mean() 

    # 앞부분(START) 자르고 채팅 빈도순으로 정렬하기
    processed_data = moving_avg.drop(list(range(1,START))).sort_values(ascending=[False])

    return moving_avg, processed_data   # 그래프 x축, 전처리된 데이터 반환


# TERM: 단편 하이라이트의 최소 길이 (default: 10sec)
# LENGTH: 전체 하이라이트 길이 (default: 10min)
def find_highlight(data, TERM=10, LENGTH=60*10):
    H=[]
    hileng=0
    num=0
    while(hileng<LENGTH and num<len(data)):
        hileng=0
        peaktime=data.index[num]
        H.append((max(peaktime-TERM,0), peaktime))
        H.sort()
        try:
            for i in range(0,len(H)):
                while (True):
                    if H[i][1] >= H[i+1][0]:
                        if H[i][1] <= H[i+1][1]:
                            H[i]=(H[i][0],H[i+1][1])
                        del H[i+1]
                    else:
                        break
        except IndexError:
            for t in H:
                hileng += t[1]-t[0]
        num+=1

    return H, hileng    # 하이라이트 구간, 전체길이 반환


def print_result(highlight, leng):
    for i, (left, right) in enumerate(highlight):
        print('['+str(i+1)+'] ' + str(datetime.timedelta(seconds=int(left))) + ' ~ ' + 
        str(datetime.timedelta(seconds=int(right))))
    print("하이라이트 개수: " + str(len(highlight)))
    print("전체 하이라이트 길이: " + str(leng))


def visualization(x, path):
    x.plot(figsize=(50,15), grid=True, title="Catch Highlights")
    plt.xlabel("sec")
    plt.savefig(path)


def return_json(moving_avg, result_path):
    temp = moving_avg.to_dict()
    result_json = [[k, v] for k, v in temp.items()]
    with open(result_path, 'w') as outfile: 
            json.dump(result_json, outfile)


# MAIN
def main(argv):
    print("x")
    video_id = argv[1]
    raw_path = "./python/Data/raw_data/"+video_id+".json"
    result_path = "./python/Data/result_data/"+video_id+".json"
    graph_path = "./python/Data/graph_data/"+video_id+".png"
    print("x")
    with open(raw_path, encoding='UTF-8') as jFile:
        json_data = json.load(jFile)

    # 채팅 데이터에서 각 시간별 채팅 빈도수만 뽑아서 반환
    chat_count = check_frequency(json_data)          

    # 데이터를 전처리하여 사용할 채팅 빈도수만 골라 반환 
    ## moving_average: 이동평균 데이터
    ## 전처리: 이동평균 적용, 앞부분 슬라이싱, 정렬
    moving_avg, preprocessed_data = data_preprocessing(chat_count)

    # 실제 하이라이트 구간, 전체 길이 반환
    highlight, leng = find_highlight(preprocessed_data)
    print(highlight, leng)

    # 결과 출력
    print_result(highlight, leng)

    # 그래프 저장
    visualization(moving_avg, graph_path)

    # 이동평균 결과 JSON 반환
    return_json(moving_avg, result_path)

if __name__ == "__main__":
    main(sys.argv)