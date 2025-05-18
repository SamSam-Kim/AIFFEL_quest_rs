# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성훈
- 리뷰어 : 권재현


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 1. ResNet-34, ResNet-50 모델 구현이 정상적으로 진행되었습니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_9.png?raw=true">
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_10.png?raw=true">
    - 2. 구현한 ResNet 모델을 활용하여 Image Classification 모델 훈련이 가능합니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_11.png?raw=true">
    - 3. Ablation Study 결과가 바른 포맷으로 제출되었습니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_12.png?raw=true">
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - bottle neck block을 구체적으로 잘 구현하였고, 작동 방식을 이해할 수 있도록 주석을 작성하였습니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_13.png?raw=true">
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 추가 실험을 진행하여 다른 데이터셋에 대해서는 모델이 어떻게 학습되는지를 비교 및 분석하였습니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_14.png?raw=true">
        
- [O]  **4. 회고를 잘 작성했나요?**
    - 전체 실험 결과를 구체적으로 분석하여서 결론에 작성해 놓았고 개선 방안을 심사숙고하여 도출하였습니다.
        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 3번에 작성한 사진의 알부분인데, 효울적인 알고리즘으로 bottle neck block을 구현하였습니다.
        - <img src = "https://github.com/bluegold75/AIFFEL_QUEST_RS/blob/main/image/sam_15.png?raw=true">


# 회고(참고 링크 및 코드 개선)
- 1. 라이브러리 버전, 모델 구조 확인, 이미지 예시 확인 등 꼼꼼한 접근이 돋보였습니다.
- 2. Ablation Study를 위한 그래프 확인, Accuracy 및 Loss를 성공적으로 확인하였습니다.
- 3. 기존 학습 방식의 문제점을 단순히 발견한데서 그치지 않고 추가 실험을 진행하여서 의미있는 결과를 도출하였습니다.
- * 전체적으로 세밀하고 꼼꼼한 접근을 통해 완벽한 실험 및 분석을 진행하였습니다. 
