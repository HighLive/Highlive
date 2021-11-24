from collections import Counter
def check_frequency(json_data):
    timeData = []
    for chat in json_data:
        timeData.append(int(json_data[chat]['time']))

    freq = Counter(timeData)
    temp = pd.Series(freq)
    chat_count = temp.reindex(list(range(1, temp.last_valid_index() + 1)), fill_value=0)

    return chat_count  # 시간대별 채팅 수 반환