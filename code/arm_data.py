import cv2  # OpenCV: for those who like to play with images.
import mediapipe as mp  # MediaPipe: turning you into a digital puppeteer.
import numpy as np  # Numpy: because who doesn't love arrays?
import serial  # Serial communication: talking to gadgets like they're old friends.

# Setting up MediaPipe drawing utilities, because hand-tracking without visuals is like pizza without cheese.
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Initializing serial port - COM3 is like that one friend you always rely on.
ser = serial.Serial(port='COM3', baudrate=9600, timeout=.1)  

# Starting video capture. Smile, you're on candid camera!
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,  # Keep it simple, no need to show off.
    min_detection_confidence=0.5,  # I'm 50% sure that's a hand.
    min_tracking_confidence=0.5) as hands:  # And 50% sure it's still there.
  
  while cap.isOpened():  # The eternal loop of video capture.
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")  # Camera shy, are we?
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, let's not mess with the image. It's perfect as it is.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR to RGB: because OpenCV likes to be different.

    results = hands.process(image)  # Let the hand tracking magic happen!

    # Alright, let's allow writing on the image again. We're not monsters.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:  # If we've got some hands...
        for hand_landmarks in results.multi_hand_landmarks:
            # Calculating wrist coordinates, because why not?
            coordX = (np.round(0.5 - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x, 3)) * 1000
            coordY = (np.round(0.5 - hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y, 3)) * 1000
            coordZ = np.round(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].z, 3)
            
            # Uncomment for exclusive X coordinate party.
            #if coordX >= 0.25 or coordX <= -0.25:  
            print(f'[{coordX}, {coordY}, {coordZ}]')  # Broadcasting wrist coordinates to the world.
            ser.write(f"{coordX},{coordY}\n".encode())  # Sending secret wrist messages to serial port.

            # Drawing the hand landmarks because hands are beautiful.
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
    
    # Flip the image horizontally for a mirror effect. Who's that good-looking person there?
    cv2.imshow('Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to escape this hand-tracking madness.
      break

# Cleaning up the mess. Close serial and release the camera.
ser.close()
cap.release()
