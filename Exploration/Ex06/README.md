# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성훈
- 리뷰어 : 조성호


# PRT(Peer Review Template)
- [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 예
    - 추론적 요약과 추출적 요약을 모두 사용해 요약문을 확인할 수 있는 코드가 제출되었다.
![image](https://github.com/user-attachments/assets/33b64bb2-feba-4d53-b5a1-163ab34c1a6f)

    
- [ ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 예
    - 모델링 코드를 인코더, 디코더, 어텐션 모두 합친 뒤 각각을 표시해둔 것이 이해하기 쉬웠다.
![image](https://github.com/user-attachments/assets/63245801-231b-49df-9d0f-cc74f9b47d88)

        
- [ ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 예
    - outlier 확인하는 추가실험 진행
![image](https://github.com/user-attachments/assets/8146bde4-a8eb-464d-a9b3-0208e55e0204)

    - 여러 헤드라인에 대해 비교 실험
![image](https://github.com/user-attachments/assets/0750f7b7-7dd6-44d2-b592-bc33b38c7ec3)

    - 한 문장에서 추출적 요약 가능 여부 확인
![image](https://github.com/user-attachments/assets/47631944-db0c-459d-b948-f217541ae0b8)

    - 실제 뉴스 기사에 추출적 요약 적용
![image](https://github.com/user-attachments/assets/1da071ba-a4cd-4376-ade1-d33c90176ae3)

- [ ]  **4. 회고를 잘 작성했나요?**
    - 예
    - 추상적 요약과 추출적 요약의 비교를 완벽히 수행하고, 그 과정에서 알게 된 지식을 바탕으로 회고를 작성함.
![image](https://github.com/user-attachments/assets/2a8a1b0b-23ec-4b97-a967-f48b4b7b9de6)

        
- [ ]  **5. 코드가 간결하고 효율적인가요?**
    - 예
    - 샘플 길이 분포를 확인하는 함수 작성
![image](https://github.com/user-attachments/assets/4ad2dc81-4652-417e-975f-8e43ce80835c)
    - 실제 헤드라인과 추론적 요약 헤드라인의 비교 함수 작성
![image](https://github.com/user-attachments/assets/b8455775-6d46-46fe-b4c9-fc384bac0818)
    - 추출적 요약까지 비교하는 함수 작성
![image](https://github.com/user-attachments/assets/d8c8836a-70ba-4575-a03d-f282df9a07fe)



# 회고(참고 링크 및 코드 개선)
```
제가 실험하지 못한 다양한 추가 실험을 해 주셔서 많이 배웠습니다.
반복적으로 사용되는 코드를 대부분 함수화하여 여러 상황에 대해 실험해보는 부분이 좋았습니다.
데이터 전처리 부분에서도 저와 달리 샘플을 직접 확인해보기도 하고,
길이를 다양하게 조절하며 데이터 양을 적절히 조절하는 것을 보며 정성이 느껴졌습니다.
사소한 코드라도 조금씩 바꿔가며 코드의 길이나 실행 속도 면에서 어떻게 바뀌는지 확인해보신 것을 다음 퀘스트에서 본받겠습니다!
```
