import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

# Parameters
width, height = 1280, 720


# Webcam
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Hand detector
detector = HandDetector(maxHands=2, detectionCon = 0.8)

#Communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1",5052)

while True:
  sucess, frame = video_capture.read()
  hands, frame = detector.findHands(frame)

  data = []

  if hands:
    hand = hands[0]
    lmList = hand['lmList']
    # print(lmList)
    for lm in lmList:
      data.extend([lm[0], height - lm[1], lm[2]])
    # print(data)
    sock.sendto(str.encode(str(data)), serverAddressPort)


  cv2.imshow("screen", frame)
  if cv2.waitKey(1) == ord('q'):
      break
cv2.destroyAllWindows()
