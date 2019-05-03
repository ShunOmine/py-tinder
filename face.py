import cv2

#Haar-like 特徴分類機の読み込み
face_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')

#イメージファイルの読み込み
img = cv2.imread('profile.img.03.jpg')

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔を検知
faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()