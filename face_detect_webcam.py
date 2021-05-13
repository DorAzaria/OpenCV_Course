import cv2

faceCascade = cv2.CascadeClassifier('haar_face.xml')

# This line sets the video source to the default webcam, which OpenCV can easily capture.
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.putText(frame, 'Dor Azaria', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv2.rectangle(frame, (x, y+10), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
