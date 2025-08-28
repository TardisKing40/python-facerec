# Get basic requirements
import cv2
import face_recognition

# Set default video capture
video_capture = cv2.VideoCapture(0)

# Run continuously 
while True:
    # Read the current frame
    frame = video_capture.read()[1]
    # Get the location of each face on the screen
    face_locations = face_recognition.face_locations(frame)
    
    # For every face
    for face_location in face_locations:
        # Set their individual left,right,up,down
        top, right, bottom, left = face_location
        # Set a rectangle outline
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display video to camera
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release() # Stop capturing camera
cv2.destroyAllWindows() # Destroy window
