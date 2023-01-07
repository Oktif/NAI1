'''
Computer Vision
Programming team : Oktawian Filipkowski, Maciej Zakrzewski
In this exercise we need to create an app which will monitor if user is watching
commercial.
If he stops watching commercial will be paused and sound warning will be played.
After that warning image will be displayed and user will be forced to press any key to
continue watching ad.

Since we are using Haar Cascade frontalface.xml app will stop recognizing
user if he doesn't look at camera, which will pause an AD.
'''

'''
We start with importing and using Haar Cascade face detection pretrained model 
'''
import cv2
import winsound

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

'''
Setting countdown for starting video
'''
count = 0

'''
Reading files:
video camera for user monitoring
our 'ad' video
warning image
'''
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture('videoplayback.mp4')
img2 = cv2.imread('image.jpg')

frm2 = None
'''
Checking if video files are present
'''
if cap1.isOpened() == False:
    print("Error Camera Not Found")
if cap2.isOpened() == False:
    print("Error File Not Found")

'''
If they are present we proceed to launching
'''
while cap2.isOpened():
    ret1, frm1 = cap2.read()
    if ret1 == True:
        if ret1:
            '''
            Monitoring user and add launching,
            slight delay between two
            '''
            if count > 5:
                if cap2.isOpened():
                    _, frm2 = cap2.read()

            if frm2 is not None:
                cv2.imshow("frm2", frm2)

            if frm1 is not None:
                ret, img = cap1.read()
                '''
                Grayscale
                '''
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                '''
                Using trained face detection algo
                '''
                detected_faces = face_classifier.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5,minSize=(20, 20))
                detected_eyes = eye_classifier.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=4, minSize=(10, 10))

                '''
                Drawing rectangles on user face
                '''
                for (x, y, width, height) in detected_faces:
                    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 10)

                for (x, y, w, h) in detected_eyes:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
                '''
                Monitoring user frame-by-frame
                For privacy reasons this option is turned off in presentation
                '''
                cv2.imshow("frm1", img)

            key = cv2.waitKey(1)

            '''
            If user is not focusing on monitor/camera AD will be stopped,
            warning sound will be played
            and warning message will appear
            to proceed user must press a key.
            '''
            if detected_eyes == () and detected_faces == ():
                winsound.Beep(440, 500)
                cv2.imshow('img', img2)
                cv2.waitKey(-1)  # wait until any key is pressed
                cv2.destroyWindow("img")

        count += 1

    else:
        break

'''
Closing windows and stopping monitoring after ad is played
'''
cap2.release()
cv2.destroyAllWindows()
