from enum import Enum

# java process builder를 통해 실행시킬 경우 다음의 경로를 따라야 함
class Path(Enum):
    raw = "./python/Data/raw_data/"
    traffic = "./python/Data/traffic_data/"
    highlight = "./python/Data/highlight_data/"
    emotion = "./python/Data/emotion_data/"
    valid = "./python/Data/valid_data/"
    graph = "./python/Data/graph_data/"
