# yolo-v1-pytorch
yolo v1 pytorch (resnet18 사용하게 수정)


data/VOC_allimgs 폴더에 Pascal voc 2007, 2012이미지 전부 넣으면 됨

train_yolo.py : 모델 학습, results 폴더에  3epoch마다 weight 저장 (총 135epoch)


training 끝난 후

evaluate.py : 저장된 weight들 각각에 대해 MAP 측정, MapList.txt에 기록
plottest.py : MapList.txt 이용해서 간단한 그래프

detect.py : weight 이용해서 이미지에 대해 bbox 그려서 result.png로 저장

주의 : weight(~.pth파일) 경로들은 코드 내에서 알아서 잘 수정해서 쓰면 됨


135 epoch 학습시킨 weight 파일
https://drive.google.com/file/d/1ZUeYlqmA1Y4Q7CleZX45ALBVsgbZ4sWZ/view?usp=sharing
