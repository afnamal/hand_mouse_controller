import cv2
import mediapipe as mp
import pyautogui

# Initialize mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Define screen width and height
screen_width, screen_height = pyautogui.size()

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of index finger tip and thumb tip
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert the coordinates to screen space
            index_x = screen_width - int(index_finger_tip.x * screen_width)
            index_y = int(index_finger_tip.y * screen_height)
            thumb_x = screen_width - int(thumb_tip.x * screen_width)
            thumb_y = int(thumb_tip.y * screen_height)

            # Move the mouse cursor to the index finger tip position
            pyautogui.moveTo(index_x, index_y)

            # Check if the thumb and index finger tips are close to each other (click)
            if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
                pyautogui.click()

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
