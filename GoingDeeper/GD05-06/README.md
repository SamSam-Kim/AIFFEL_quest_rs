# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성훈
- 리뷰어 : 권재현


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 1. ResNet50 + GAP + DenseLayer 결합된 CAM 모델의 학습과정이 안정적으로 수렴하였습니다.
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_1.png?raw=true">
    - 2. CAM 방식과 Grad-CAM 방식의 class activation map이 정상적으로 얻어지며, 시각화하였을 때 해당 object의 주요 특징 위치를 잘 반영하였습니다.
    - 3. CAM과 Grad-CAM 각각에 대해 원본이미지합성, 바운딩박스, IoU 계산 과정을 통해 CAM과 Grad-CAM의 object localization 성능이 비교분석되었습니다.

- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 모델 생성부분에 특히 상세한 주석을 달아놓았습니다.
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_6.png?raw=true">

        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 1. 추가 실험을 다양하게 시도하였습니다.(한 사진으로 Threshold값 비교 및 다른 사진들로 다시 진행, CAM 및 Grad-CAM 비교 등)
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_4.png?raw=true">
    - 2. 실험 과정에서 생긴 합성 에러를 해결하였습니다.(밑에가 합성 에러)
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_2.png?raw=true">
    - 3. 모델이 예측하는 바운딩 박스에 의문을 제기하고, IOU 계산식을 수정하였습니다.(1번 그림에도 나타납니다.)
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_3.png?raw=true">
    - 4. 각 convolution layer가 출력하는 activation map을 출력하고, 추가 실험을 진행하였습니다.
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_5.png?raw=true">
        
- [O]  **4. 회고를 잘 작성했나요?**
    - 1. 결론 및 회고를 상세하게 작성하였습니다.
    - 2. 결론 및 회고를 통해 리뷰어가 인사이트를 얻어갈 수 있었습니다.
        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 함수를 매우 효율적으로 간결하게 작성하였습니다.
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_7.png?raw=true">
    - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_8.png?raw=true">


# 회고(참고 링크 및 코드 개선)
- 1. 주어진 과제를 완료하는데 그치지 않고, 추가 실험을 구체적인 기준을 잘 설정하여 실행하였습니다.
- 2. 논문을 참고해서 성능을 비교 및 분석을 성공적으로 완료하였습니다.
- 3. 문제가 될 만한 부분(threshold), 양수가 나와야 되는데 음수가 나와야 되는 경우 등 에 대하여 코드를 개선하였습니다.
- 4. 전체적으로 구체적이고 정밀한 실험을 정확한 비교 및 분석을 진행하여 성공적인 인사이트를 도출하였습니다.
