# Food-Recognition-AI
https://tiwarinitin1999.medium.com/yolov3-custom-object-detection-with-transfer-learning-47186c8f166d 
해당 포스팅을 이용하여 음식 사진을 입력받아 음식의 종류를 구별하는 인공지능을 만들었습니다.

YOLOv3를 이용해 Transfer Learning을 적용하여 사용자 정의 데이터에 대한 객체 감지를 수행했습니다.

인공지능 학습에 필요한 dataset을 모으기 위하여 labelImg라는 프로그램을 사용하였으며, 자주 먹는 음식들에 관해 대략 300가지의 음식 종류 정도 인식이 가능합니다.

저의 환경은 GUI 기반의 환경이 아니므로 모든 인공지능 학습은 Google Colab을 활용하였습니다.



<파일 정리>
1. test_image : Object_Detection.py에서 실행되어질 입력받는 음식 테스트 사진들 모음
2. Obect_Detection.py : 음식 인식 인공지능을 실행하기 위한 주요 파일 (이 파일로 실행을 진행함)
3. classes.txt : 인공지능이 인식 가능한 음식 종류
4. yolov3_training_last.weights : 학습 결과에 대한 가중치 파일

