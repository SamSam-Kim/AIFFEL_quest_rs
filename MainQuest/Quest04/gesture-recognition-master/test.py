import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

# --- 설정 부분 (변경 없음) ---
actions = ['come', 'away', 'spin']
seq_length = 30
model = load_model('models/model2_1.0.h5')

# MediaPipe hands model 초기화 (변경 없음)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# --- ★★★ 코드 변경 지점 1: VideoCapture 설정 ★★★ ---
# 기존 웹캠 코드: cap = cv2.VideoCapture(0)
# 변경된 코드: 동영상 파일 경로를 입력합니다.
# 파일 이름은 실제 가지고 계신 동영상 파일 이름으로 바꿔주세요. (예: 'my_gestures.mp4')
video_path = './video/cat.mp4'  # <--- 여기에 사용할 동영상 파일 경로를 넣으세요!
cap = cv2.VideoCapture(video_path)

# 동영상 파일이 제대로 열렸는지 확인하는 코드 추가 (권장)
if not cap.isOpened():
    print(f"오류: 동영상 파일 '{video_path}'을(를) 열 수 없습니다.")
    exit()

# --- 주석 처리된 비디오 저장 부분은 그대로 둡니다 (변경 없음) ---
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# out = cv2.VideoWriter('input.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (w, h))
# out2 = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (w, h))

seq = []
action_seq = []

while cap.isOpened():
    ret, img = cap.read()
    
    # --- ★★★ 코드 변경 지점 2: 동영상 종료 처리 ★★★ ---
    if not ret:
        print("동영상의 끝에 도달했습니다. 프로그램을 종료합니다.")
        break  # 동영상이 끝나면 루프를 빠져나감

    # img0 = img.copy() # 원본 프레임을 저장하는 코드는 필요 없으므로 주석 처리하거나 삭제 가능

    # --- 이하 로직은 대부분 동일합니다 (변경 없음) ---
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 4))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z, lm.visibility]

            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3]
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3]
            v = v2 - v1
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:]))
            angle = np.degrees(angle)

            d = np.concatenate([joint.flatten(), angle])
            seq.append(d)

            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

            if len(seq) < seq_length:
                continue

            input_data = np.expand_dims(np.array(seq[-seq_length:], dtype=np.float32), axis=0)
            y_pred = model.predict(input_data).squeeze()
            i_pred = int(np.argmax(y_pred))
            conf = y_pred[i_pred]

            if conf < 0.9:
                continue

            action = actions[i_pred]
            action_seq.append(action)

            if len(action_seq) < 3:
                continue

            this_action = '?'
            if action_seq[-1] == action_seq[-2] == action_seq[-3]:
                this_action = action

            cv2.putText(img, f'{this_action.upper()}', org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

    cv2.imshow('img', img)

    # --- ★★★ 코드 변경 지점 3: waitKey 지연 시간 조절 ★★★ ---
    # 실시간 웹캠에서는 1ms로 충분하지만, 동영상은 원래 속도에 맞게 재생하는 것이 자연스럽습니다.
    # 보통 25 또는 33 (30~40fps 기준)을 사용합니다. 
    # 1로 두면 동영상이 매우 빠르게 재생됩니다.
    if cv2.waitKey(25) == ord('q'):
        break

# --- 루프 종료 후 자원 해제 (추가 권장) ---
cap.release()
cv2.destroyAllWindows()