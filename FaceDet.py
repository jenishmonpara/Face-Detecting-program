import cv2

cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret, frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

    for face in faces:
        x,y,h,w = face
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow("Jenish's window",frame)

    key = cv2.waitKey(20)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

