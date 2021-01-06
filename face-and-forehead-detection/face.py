import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('The-Big-Bang-Theory-Season-12.jpeg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # Detect eyes
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
# Draw rectangle around the faces
index = 1
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # cv2.rectangle(img, ())
    text = "Person " + str(index)
    index += 1
    cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

    # Marking the forehead
    roi = img[y + 10:y + h - 80, x + 35:x + w - 25]

    cv2.rectangle(img, (x + 35, y + 10), (x + w - 25, y + h - 80), (0, 0, 255), 2)

    foo = cv2.mean(roi)

    print(text + "_RGB", end='= ( ')
    print(foo[2], ',', foo[1], ',', foo[0], ')')

    # roi_gray = gray[y:y+h, x:x+w] 
    # roi_color = img[y:y+h, x:x+w] 

    # # Detects eyes of different sizes in the input image 
    # eyes = eye_cascade.detectMultiScale(roi_gray)  



    # #To draw a rectangle in eyes 
    # for (ex,ey,ew,eh) in eyes: 
    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 

# Display the output
cv2.imshow('img', img)
cv2.waitKey()