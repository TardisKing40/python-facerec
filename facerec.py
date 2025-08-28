import cv2
import face_recognition

video_capture = cv2.VideoCapture(0)

while True:
    frame = video_capture.read()[1]
    face_locations = face_recognition.face_locations(frame)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
