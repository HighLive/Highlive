# HighLive
![image](https://user-images.githubusercontent.com/28651727/143378920-175f9850-a091-4ed7-82cc-50d0a3cf3c1f.png)

http://3.38.119.154:8080/

*python dependency*

- pandas
- matplotlib
- requests

## Usage

트위치에 업로드된 동영상에 대한 URL을 상단 입력폼에 입력하면 해당 동영상에 대한 분석 결과를 확인하실 수 있습니다.

ex) https://www.twitch.tv/videos/1210752959

## Development Goal

동영상에 음성과 시각 데이터만 있었던 과거와는 달리 현재는 1인 방송 플랫폼의 등장으로 시청자들로 부터 채팅 데이터를 얻을 수 있습니다.  
이러한 채팅데이터를 활용하여 **분석한 데이터를 제공**하고, 추후에는 이러한 분석데이터를 토대로 편집자의 개입 없이 주요장면을 구별하고 매끄럽게 이어붙이는 컷편집의 단순 반복 작업을 자동화 하여 하이라이트 영상을 제공하는 것을 목표로 삼았습니다.

## Implementation
![image](https://user-images.githubusercontent.com/28651727/143439790-9d71db92-7e9e-4497-ae50-5f588c096ead.png)

- 사용자가 웹브라우저를 통해 트위치동영상의 url을 입력하고, 스프링의 내장 톰캣서버를 통해 이를 전달받아 파이썬 분석 모듈을 실행시킵니다. 
- 파이썬 모듈은 해당 영상에 대한 분석데이터들을 json데이터 형태로 저장을하고 결과페이지를 출력합니다.
- 결과페이지는 저장된 json 파일을 통해 분석결과를 제공합니다.
- **캐시**를 구현하여 한번 분석된 데이터는 곧바로 제공하도록 하였습니다.

## Future Work

1. json 분석데이터에데한 데이터베이스 구축
2. 자연어 처리 라이브러리를 채팅에 최적화 하여 적용
3. CNN알고리즘을 통해 영상을 통한 하이라이트 분류 모델 구현
4. 트위치 뿐만 아니라 Youtube, AfreecaTV등 다양한 영상 플랫폼을 활용할 수 있도록 개선
5. 편집자 개입없이 분석된 데이터를 토대로 추출된 하이라이트 구간을 모아 사용자에게 제공하는 자동 편집 기능 추가

## Members

- waterfogSW(FE/BE)
- rilac1(FE/BE)
- jinHur(FE/BE)

