import cv2
import numpy as np
from keras.models import load_model
classifier = load_model('Trained_model.h5')
from keras.preprocessing import image
image_x, image_y = 64,64
def nothing():
        pass
class Videocamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def g_frame(self):
        img_counter = 0
        img_text = ''
        ret, frame=self.video.read()
        frame = cv2.flip(frame,1)
        l_h = 0
        l_s = 50
        l_v = 31
        u_h = 179
        u_s = 255
        u_v = 255
        img = cv2.rectangle(frame, (425,100),(625,300), (0,255,0), thickness=2, lineType=8, shift=0)
        imcrop = img[102:298, 427:623]
        lower_blue = np.array([l_h, l_s, l_v])
        upper_blue = np.array([u_h, u_s, u_v])
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        test_image = image.load_img('1.png', target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = classifier.predict(test_image)
        if result[0][0] == 1:
            img_text='A'
        elif result[0][1] == 1:
            img_text='B'
        elif result[0][2] == 1:
            img_text='C'
        elif result[0][3] == 1:
            img_text='D'
        elif result[0][4] == 1:
            img_text='E'
        elif result[0][5] == 1:
            img_text='F'
        elif result[0][6] == 1:
            img_text='G'
        elif result[0][7] == 1:
            img_text='H'
        elif result[0][8] == 1:
            img_text='I'
        elif result[0][9] == 1:
            img_text='J'
        elif result[0][10] == 1:
            img_text='K'
        elif result[0][11] == 1:
            img_text='L'
        elif result[0][12] == 1:
            img_text='M'
        elif result[0][13] == 1:
            img_text='N'
        elif result[0][14] == 1:
            img_text='O'
        elif result[0][15] == 1:
            img_text='P'
        elif result[0][16] == 1:
            img_text='Q'
        elif result[0][17] == 1:
            img_text='R'
        elif result[0][18] == 1:
            img_text='S'
        elif result[0][19] == 1:
            img_text='T'
        elif result[0][20] == 1:
            img_text='U'
        elif result[0][21] == 1:
            img_text='V'
        elif result[0][22] == 1:
            img_text='W'
        elif result[0][23] == 1:
            img_text='X'
        elif result[0][24] == 1:
            img_text='Y'
        elif result[0][25] == 1:
            img_text='Z'

        cv2.putText(frame, img_text, (30, 400), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 255, 0))
        img_name = "1.png"
        save_img = cv2.resize(mask, (image_x, image_y))
        cv2.imwrite(img_name, save_img)
        print("{} written!".format(img_name))
        #img_text = predictor()
        
       
        

        
 


        ret,jpeg=cv2.imencode(' .jpg',frame)
        return jpeg.tobytes()
    