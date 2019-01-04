import cv2     ''' import opencv  functions'''
vid_cam = cv2.VideoCapture(0)        ''' opens the webcam , 0 for default camera and 1 for external camera'''
 face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    ''' algorithm that detects faces (analyse more in this topic)'''
 face_id =  raw_input()  ''' setting id for face (any integer number)'''
count = 0  '''variables should be initialized'''
while(vid_cam.isOpened()): ''' checks if the webcam is operating ,if true then while loop executes'''
    ret, image_frame = vid_cam.read() ''' initializing the webcam feed to variables'''
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)  ''' conversion of color to grayscale (black and white)'''
    faces = face_detector.detectMultiScale(gray, 1.3, 5)  ''' detecting the portions in the face that represents the face such as nose,eyes and mouth'''
    for (x,y,w,h) in faces:  
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2) ''' try to understand this portion your own and fill the comment here'''
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w]) ''' saving the image in screen with tags of faceid,count no of image and extension name'''
        cv2.imshow('frame', image_frame) '''shows the webcam feed'''
    if cv2.waitKey(100) & 0xFF == ord('q'):   ''' wait key enables the frame to stay on screen and pressing Q BUTTON exits the window'''
        break
    elif count>100:
        break
vid_cam.release() 
cv2.destroyAllWindows()
