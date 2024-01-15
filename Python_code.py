import cv2
import mediapipe as mp
import serial as srl
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open the webcam (you may need to change the index based on your setup)
cap = cv2.VideoCapture(0)

# Open the serial connection (you may need to change the port)
ser_connection = srl.Serial('COM5', 9600, timeout=1)

# Variable to store the previous finger count
prev_num_fingers = 0

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract x, y coordinates of the hand landmarks
            landmarks_list = []
            for point in hand_landmarks.landmark:
                height, width, _ = frame.shape
                x, y = int(point.x * width), int(point.y * height)
                landmarks_list.append((x, y))

            # Count the number of fingers shown
            num_fingers = 0
            if landmarks_list[4][1] < landmarks_list[3][1]:
                num_fingers += 1
            if landmarks_list[8][1] < landmarks_list[7][1]:
                num_fingers += 1
            if landmarks_list[12][1] < landmarks_list[11][1]:
                num_fingers += 1
            if landmarks_list[16][1] < landmarks_list[15][1]:
                num_fingers += 1
            if landmarks_list[20][1] < landmarks_list[19][1]:
                num_fingers += 1

            # Display hand position and finger count on the frame
            cv2.putText(frame, f"Hand Position - X: {landmarks_list[0][0]}, Y: {landmarks_list[0][1]}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f"Fingers: {num_fingers}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Check if the finger count has changed
            if num_fingers != prev_num_fingers:
                # Send the number of fingers to the ESP32 only if it has changed
                ser_connection.write(f"{num_fingers}\n".encode())

            # Update the previous finger count
            prev_num_fingers = num_fingers

    # If no hands are detected, send '0' to the ESP32
    else:
        # Check if the finger count has changed
        if prev_num_fingers != 0:
            # Send '0' only if the finger count has changed
            ser_connection.write(b"0\n")

        # Update the previous finger count
        prev_num_fingers = 0

    # Display the resulting frame
    cv2.imshow('Hand Position', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the serial connection
cap.release()
ser_connection.close()
cv2.destroyAllWindows()
