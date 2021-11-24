import datetime
import pandas as pd
from collections import Counter

# 시간대별 채팅 수 반환
def check_frequency(json_data):
    timeData = []
    for chat in json_data:
        timeData.append(int(json_data[chat]['time']))

    freq = Counter(timeData)
    temp = pd.Series(freq)
    chat_count = temp.reindex(list(range(1, temp.last_valid_index() + 1)), fill_value=0)

    return chat_count


# 이동평균 적용결과 반환
def data_preprocessing(input_data, START=0, WIN=7):
    # 앞부분 자르기(START)
    sliced = input_data.drop(range(1,START))
    
    # 이동평균 적용(WIN)
    moving_avg_data = sliced.rolling(WIN).mean()
    moving_avg_data[range(WIN-1)] = 0    # NaN 제거
    return moving_avg_data


# 하이라이트 측정결과 반환
def find_highlight(input_data, TERM=10, LENGTH=60 * 10):
    ## TERM: 하이라이트 단편 최소 길이
    ## LENGTH: 하이라이트 총 길이

    # 채팅 빈도순으로 정렬
    sorted_data = input_data.sort_values(ascending=[False])

    H = []
    hileng = 0
    num = 0
    while (hileng < LENGTH and num < len(sorted_data)):
        hileng = 0
        peaktime = sorted_data.index[num]
        H.append((max(peaktime - TERM, 0), peaktime))
        H.sort()
        try:
            for i in range(0, len(H)):
                while (True):
                    if H[i][1] >= H[i + 1][0]:
                        if H[i][1] <= H[i + 1][1]:
                            H[i] = (H[i][0], H[i + 1][1])
                        del H[i + 1]
                    else:
                        break
        except IndexError:
            for t in H:
                hileng += t[1] - t[0]
        num += 1

    return H, hileng  # 하이라이트 구간, 전체길이 반환



def print_result(highlight, leng):
    for i, (left, right) in enumerate(highlight):
        print('['+str(i+1)+'] ' + str(datetime.timedelta(seconds=int(left))) + ' ~ ' +
        str(datetime.timedelta(seconds=int(right))))
    print("Number of highlights: %d" % len(highlight))
    print("Full length of highlight: %dmin %dsec" % (leng//60, leng%60))


def main(argv):
    chat_count =  check_frequency(shared_log)
    moving_avg_data = data_preprocessing(chat_count)
    highlight_data, leng = find_highlight(moving_avg_data)
    highlight_data.print_result(highlight, leng)
    return_json(moving_avg_data, path['traffic_data'])
    return_json(highlight_data, path['highlight_data'])