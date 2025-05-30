# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성훈
- 리뷰어 : 반태훈


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 네!!
    - ![image](https://github.com/user-attachments/assets/80464ce7-1927-419e-ac2c-9b55a1af53d9)
    - ![image](https://github.com/user-attachments/assets/fdca824d-600a-4778-9101-169575324cf7)
    - ![image](https://github.com/user-attachments/assets/4c9b1bff-ef39-4852-89cd-c7d632496870)
    - ![image](https://github.com/user-attachments/assets/5593aa95-b376-4713-88cb-b3edbf3f31d5)
    - ![image](https://github.com/user-attachments/assets/84f10ec9-1ad8-47be-b946-492fe79d9472)
    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 네!
        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - ![image](https://github.com/user-attachments/assets/43cd301b-5401-4484-bbac-f2e96259a5e1)
     
    - (추가실험)
    - ![image](https://github.com/user-attachments/assets/3bfd88c5-3a71-4778-92b5-5aae7665d1c0)
    - SBL의 경우:
    - 좌우 어깨, 손목, 팔꿈치, 무릎, 발목을 각각 한 지점으로 추론했다.
    - ![image](https://github.com/user-attachments/assets/b3b508e5-c12b-419a-bce9-c4c9c64d4612)
    - ![image](https://github.com/user-attachments/assets/4d204e45-0d4f-469d-aab0-0b0bb3a89a79)
    - ![image](https://github.com/user-attachments/assets/07f85cdd-ac86-40e5-9764-2e16cdb63b70)


      
# 시각화 비교 결과
- 두 모델 모두 좌우 구분을 잘 못하지만 그나마 SHG모델은 어느 정도 구분해내는 편이다.

- 두 모델 모두 이미지 내에서 한 명 밖에 인지하지 못한다.

Detection 모델로 크롭한 이미지 내에서 KeyPoint를 찾는 2 stage 방식을 고려해 봐야 겠다.
SHG 모델은 다리에서 색상이나 경계선 등을 기준으로 발목을 구분하는 경향이 있다.

부츠 윗 부분 무릎을 반복적으로 발목이라고 오인식하는 사례를 관측했다.
SHG 모델은 위치와 거리상 불가능한 자세를 추정 결과로 출력하기도 한다.

편견없이 그런 결과를 내는 걸 보면 복잡한 모델의 구조 등으로 인해 특정 특성에 대한 편향성을 줄이는 효과를 받은 것 같다.
이는 학습 상황에서 일반화 성능을 끌어올리는 효과를 기대할 수 있겠지만 5 epoch라는 과소 적합 상태에서는 오히려 괴상한 자세를 추정하는 효과를 보인 것 같다.
SBL 모델은 좌우를 구분하지 못하는 경우가 많지만, 좌우 구분 없이 각 포인트를 비교적 잘 잡아내는 특징을 보였다.

기준에 따라 어느 모델이 우월하다는 판단이 달라지겠지만, 좌우를 제외하고 각 키포인트에 대해 비교적 잘 예측이 가능한 SBL이 실용성이 더 높다고 할 수 있겠다.
        
- [x]  **4. 회고를 잘 작성했나요?**
    - ![image](https://github.com/user-attachments/assets/7aa722d9-c4ae-4fb7-9975-4694e5c0d248)
    - ![image](https://github.com/user-attachments/assets/c59532e7-c2ac-46c2-bb02-fead87feb3a2)


        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부


# 회고(참고 링크 및 코드 개선)
```
# 다양한 실험을해주셔서 많은 인사이트를 얻을 수 있었습니다.
# 전처리 클래스(Preprocessor)는 학습과 추론 상황을 명확히 분기하여 유연한 데이터 처리가 가능하도록 잘 설계되어 있습니다.
# crop_roi 함수에서 keypoint를 기준으로 ROI를 자동 조절하는 방식이 효과적이며, 학습 성능 향상에 기여할 수 있습니다.
# 전반적으로 변수명이 직관적이고, 코드 흐름이 깔끔하게 구성되어 있는 것 같고 특히 loss 값 차이가 많이나는 것을 보고 Hourglass 모델의 loss값을 4로 나누어 simplebaseline 모델을 비교분석 한 모습도 인상적이였습니다
# 대단하시네요!!!!
```
