import cv2
import mediapipe as mp
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
screen_width , screen_hieght = pyautogui.size()

prev_x, prev_y = 0, 0
smoothening = 7

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands =1)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)
    h, w, _ = img.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm = hand_landmarks.landmark[8]
            tb = hand_landmarks.landmark[4]
            x2 = tb.x
            y2 = tb.y
            x = int(lm.x *w)
            y = int(lm.y *h)
            screen_x = lm.x * screen_width
            screen_y = lm.y * screen_hieght
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y
            cv2.circle(img, (x, y), 20, (255, 0, 0), 10)
            
            mp_draw.draw_landmarks(img , hand_landmarks, mp_hands.HAND_CONNECTIONS)

            distances = np.linalg.norm([x2 - lm.x, y2 - lm.y])
            if distances < 0.04:
                pyautogui.click()
                cv2.putText(img,"click" , (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0 ,250 ,0),2)
            

    cv2.imshow("virtual mouse", img)
    if cv2.waitKey(1) & 0xff == ord("s"):
        break
   
cap.release()
cv2.destroyAllWindows()
