import cv2 as cv
cap = cv.VideoCapture(0) # Webca
import pytesseract
import YB_Pcb_Car
import time
car = YB_Pcb_Car.YB_Pcb_Car()
def get_ocr(img):
        img_rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img_rgb)  

while True:
    is_success,img = cap.read()
    cv.imshow('Video', img)
    k = cv.waitKey(1)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
    if k % 256 == 32:
        cv.imwrite("capture.jpg" ,img)
        text_ocr =  get_ocr(img)
        print(text_ocr)   
        if "Happy" in text_ocr: 
            car.Ctrl_Servo(2,0)
            time.sleep(0.5)
            car.Ctrl_Servo(1,90)
            time.sleep(0.5)

        if "Sad" in text_ocr: 
            car.Ctrl_Servo(0,2)
            time.sleep(0.5)
            car.Ctrl_Servo(1,90)
            time.sleep(0.5)


  