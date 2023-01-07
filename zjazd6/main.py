'''
Computer Vision
Programming team : Oktawian Filipkowski, Maciej Zakrzewski
'''

'''Imports'''
import cv2
import winsound

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

'''Using video'''
video_capture = cv2.VideoCapture(0)

'''Setting video settings'''
video_capture.set(3, 640)
video_capture.set(4, 480)

'''Setting countdown for user monitoring'''
countdown = 0

'''User monitoring'''
while True:
    '''Video frame'''
    ret, img = video_capture.read()
    '''Grayscale'''
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    '''Using trained face detection algo'''
    detected_faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))
    detected_eyes = eye_classifier.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=4, minSize=(50, 50))

    '''Drawing rectangles'''
    for (x, y, width, height) in detected_faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 10)

    for (x, y, w, h) in detected_eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

    '''Beeping sound if user dont look for some time and is not focused on camera'''
    if detected_eyes == () and detected_faces == ():
        countdown +=1
        print(countdown)
        if countdown %60 == 0:
            winsound.Beep(440, 500)
            countdown = 0
    else:
        countdown = 0

    '''Title'''
    cv2.imshow('Real-Time Face Detection', img)

    '''Press esc to quit'''
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break



'''Release camera, destroy img'''
video_capture.release()
cv2.destroyAllWindows()

