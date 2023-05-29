import threading
import cv2
import imutils



# capture the video 
cap = cv2.VideoCapture(0)   # it include the no. of camera to include

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


# the read the input from the camera
_, start_frame = cap.read()
start_frame = imutils.resize(start_frame,3 width=500)
start_frame = cv2.cvtColor(start_frame,cv2.COLOR_BGR2GRAY)
# in this we convert the image into gray which help to identify 

start_frame = cv2.GaussianBlur(start_frame,(21,21),0)


# # message
alarm = False
alarm_mode = False
alarm_counter = 0

# simple function  for pop up msg
def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break

        print("KOI movement hora h baba ")
    
    alarm = False


while True:

    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)


# if we are in alarm mode we are going to calculate the differences b/w studdy and movement
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw,(5,5),0)


        # difference b/w this frame and intial start frame    and add threshold to set the limit (255 limit white)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference,25,255 , cv2.THRESH_BINARY)[1]       # buff 25 is th --255
        start_frame = frame_bw

        # using threshold we set the alarm counter if movement increase alarm counter also increase and if movement is not occur then alarm counter decrease
        if threshold.sum() > 300:
            alarm_counter +=1

        else:
            if alarm_counter >0:
                alarm_counter -=1


        # show the alarm mode active
        cv2.imshow("Cam", threshold)

    else:
        cv2.imshow("Cam", frame)
        

    if alarm_counter >20:
        if not alarm:
            alarm = True
            threading.Thread(target= print("koi movement hora h ")). start()

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0                   # to stop or toggle the alarm

    if key_pressed == ord("q"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()

