import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Finger tip landmark indices
tip_ids = [4, 8, 12, 16, 20]

# Sign language mapping based on total fingers up
sign_labels = {
    0: "Hello",
    1: "I love you",
    2: "No",
    3: "Okay",
    4: "Please",
    5: "Yes",
    6: "Great",
    7: "Peace",
    8: "Awesome",
    9: "Thank You",
    10: "Perfect"
}

# Start webcam
cap = cv2.VideoCapture(0)
print("Starting sign language detector... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    h, w, _ = frame.shape
    hand_info = {}

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            lm_list = []
            for lm in hand_landmarks.landmark:
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            label = handedness.classification[0].label  # 'Left' or 'Right'
            fingers_up = 0

            # Thumb logic
            if label == "Right":
                if lm_list[tip_ids[0]][0] < lm_list[tip_ids[0] - 1][0]:
                    fingers_up += 1
            else:  # Left hand
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                    fingers_up += 1

            # Other 4 fingers
            for i in range(1, 5):
                if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                    fingers_up += 1

            # Save count for this hand
            hand_info[label] = fingers_up

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Calculate total fingers up
    total_fingers = sum(hand_info.values())

    # Determine label
    sign_label = sign_labels.get(total_fingers, "Unknown")

    # Show per-hand counts
    if "Left" in hand_info:
        cv2.putText(frame, f'Left: {hand_info["Left"]}', (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
    if "Right" in hand_info:
        cv2.putText(frame, f'Right: {hand_info["Right"]}', (10, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Show total and label
    cv2.putText(frame, f'Total: {total_fingers}', (10, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)
    cv2.putText(frame, f'Sign: {sign_label}', (10, 270),
                cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 0, 255), 3)

    cv2.imshow("Sign Language Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
