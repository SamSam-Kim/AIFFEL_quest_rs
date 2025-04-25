# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김성훈
- 리뷰어 : 양지웅


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**  
    데이터 전처리를 통해 한글 데이터에 맞는 학습 데이터를 구축하였다.  
    ![image](https://github.com/user-attachments/assets/b17e2b25-8482-4334-bcf6-13155a11335d)

    트랜스 포머 모델을 구현하고 정상적으로 학습을 진행하였다.  
    ![image](https://github.com/user-attachments/assets/76dda039-b88f-4608-862a-ea1d77573967)
    ![image](https://github.com/user-attachments/assets/0ca94a0e-1655-456b-9896-a2b7149fb79a)

    한국어 질문을 통해 맥락에 맞는 답변을 돌려주었다.  
    ![image](https://github.com/user-attachments/assets/089becd8-9a75-40a9-b0ea-2c293ec8bf63)


- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**  
    데이터 전처리 각 부분에 대해 타당성을 잘 설명하였다. 텍스트 데이터의 전처리 기준은 사람마다 다를 수 있는데 이를 논리에 맞게 잘 설명하였다.  
    ![image](https://github.com/user-attachments/assets/8ba5b218-b7fd-4333-84d3-a3f43e017bcf)

        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**  
    입력 데이터에 여러가지 시도를 하였다. 훈련 세트에 많이 없는 주제도 넣어보며 다양한 주제로 실험했다.  
    ![image](https://github.com/user-attachments/assets/21991865-0858-4322-999d-8cadb8f8978d)

    ![image](https://github.com/user-attachments/assets/0ad19ff9-c72c-46fc-8b96-a275947fb73b)


        
- [x]  **4. 회고를 잘 작성했나요?**  
    회고와 실행 플로우를 매우 꼼꼼하게 작성해주셨다. 서로의 생각을 공유하기 편했고 실행플로우까지 첨부하여 이해하는데 도움이 많이 됐다.  
    ![image](https://github.com/user-attachments/assets/1e25f3fa-e891-4745-8003-14536e4dce60)  
    ![image](https://github.com/user-attachments/assets/2159da68-ee9c-42e5-bec5-483281bd91f0)


- [X]  **5. 코드가 간결하고 효율적인가요?**  
    데이터셋 원본 답변과 모델의 답변을 비교 출력하는 함수를 for문을 통해 효율적으로 작성하였다. 반복되는 부분을 함수와 for문으로 줄인 것이 인상적이었다.  
    ![image](https://github.com/user-attachments/assets/7edf3845-e0d4-4020-8cd0-ec603ab6d8e5)



# 회고(참고 링크 및 코드 개선)
```
다양한 시도를 해보셔서 배워갈 게 많았다. 서로 모델에서 약간씩 다른부분이 있었는데 이를 이용해서 서로의 출력을 비교해보기도 하였다.
서로 궁금한 점에 대해서 물어가면서 혼자 공부하면서 몰랐던 인사이트를 얻을 수 있었다.
회고도 꼼꼼히 작성해주셔서 깔끔하게 정리가 됐던 것 같다.
```
