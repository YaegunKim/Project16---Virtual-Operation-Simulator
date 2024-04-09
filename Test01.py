import cv2
import mediapipe as mp


video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

while True:
  sucess, frame = video_capture.read()
  if sucess:
    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(RGB_frame)
    if result.multi_hand_landmarks:
      for hand_landmarks in result.multi_hand_landmarks:
        # print(hand_landmarks)
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    


    
    
    cv2.imshow("screen", frame)
    if cv2.waitKey(1) == ord('q'):
      break
cv2.destroyAllWindows()