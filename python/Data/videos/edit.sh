#!/bin/bash

### 경로 ###
# preprocess = "./python/Data/preprocess_data/"
# videos = "./python/Data/videos/"


VIDEO_ID=$1
VIDEO_DIR_PATH=$2   # "./python/Data/videos/"
TWITCH_DL="twitch-dl"
COMMAND="$VIDEO_DIR_PATH/$TWITCH_DL"
VIDEO_ID_DIR_PATH=$VIDEO_DIR_PATH$VIDEO_ID 

PREPROCESS_DATA_PATH=$3

# 영상 다운로드
# 트위치 dl
$COMMAND download -q 480p $VIDEO_ID > ./log.txt

# 디렉터리 생성
mkdir $VIDEO_ID_DIR_PATH
touch $VIDEO_ID_DIR_PATH/$VIDEO_ID.txt
FILE_NAME=$VIDEO_ID_DIR_PATH/$VIDEO_ID.txt

# MKV 파일 이름
MKV_NAME=$VIDEO_ID_DIR_PATH/$VIDEO_ID.mkv
# mkv 파일 이동
mv ./$VIDEO_ID.mkv $VIDEO_ID_DIR_PATH/$VIDEO_ID.mkv
# 제어변수
I=0

### 방법 1, 포그라운드 실행시 자꾸 START와 TIME이 잘못 읽힘
### 백그라운드 수행 시 무리없이 잘 동작함
#while IFS='' read -r line || [[ -n "$line"  ]]; do
#    IFS=$'-'
#    temp=($line)
#    
#    START=${temp[0]}
#    TIME=${temp[1]}
#
#    echo "#############################################"
#    echo "$MKV_NAME" -ss "$START" -t "$TIME" $VIDEO_ID/test"$I".mp4
#    ffmpeg -i "$MKV_NAME" -ss "$START" -t "$TIME" $VIDEO_ID/test"$I".mp4 -nostats -loglevel 0     # 백그라운드 수행 후 인자전달 오류 해결
#    echo "$MKV_NAME" -ss "$START" -t "$TIME" $VIDEO_ID/test"$I".mp4
#    echo "#############################################"    
#
#    # video_id.txt에 file 'textname' 쓰기
#    echo file ./''test"$I".mp4'' >> $FILE_NAME
#    let I+=1
#    
#done < ../preprocess_data/$VIDEO_ID.txt

START=()
TIME=()
i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
    IFS=$'-'
	tmp=($line)
	START[${i}]=${tmp[0]}

	TIME[$[i]]=${tmp[1]}

	i=${i}+1
done < $PREPROCESS_DATA_PATH

for (( I0; I<${#START[@]}; I++)); do
    echo "#############################################"    
    echo "$MKV_NAME" -ss "${START[I]}" -t "${TIME[I]}" $VIDEO_ID_DIR_PATH/temp"$I".mp4
    ffmpeg -i "$MKV_NAME" -ss "${START[I]}" -t "${TIME[I]}" $VIDEO_ID_DIR_PATH/temp"$I".mp4 -nostats -loglevel 0     # 백그라운드 수행 후 인자전달 오류 해결
    echo "#############################################"    

    #video_id.txt에 file 'textname' 쓰기VIDEO_ID
    echo file \'temp"$I".mp4\' >> $FILE_NAME
done

echo check@@@@@@@@@@@

# concat
ffmpeg -f concat -safe 0 -i $VIDEO_ID_DIR_PATH/$VIDEO_ID.txt -c copy $VIDEO_ID_DIR_PATH/$VIDEO_ID.mp4

# temp mp4 삭제 추가


# 합치기
