import cv2
from mtcnn.detector import detect_faces
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def detect_cam_faces(countdown = 30):
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1) # 水平翻转
        image = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        draw=ImageDraw.Draw(image) #获取img的draw对象     
        draw.text((50,50), "%d" %countdown, font=ImageFont.truetype('simhei.ttf', 64),fill=(255,255,255,255)) #使用draw对象的text方法在(10,20)处使用黑体，字体大小16，白色，显示cnt对应数字
        frame=cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR)
        countdown-=1

        bounding_boxes, _ = detect_faces(image)

        for i in range(len(bounding_boxes)):
            if i>0:
                break
            cv2.rectangle(frame, (int(bounding_boxes[i][0]), int(bounding_boxes[i][1])),
                         (int(bounding_boxes[i][2]), int(bounding_boxes[i][3])), (255, 0, 0), 2)
            
        cv2.imshow('camera', frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

        if countdown==0:
            face_images = []
            if bounding_boxes is not None:
                for box in bounding_boxes:
                    box = box[:4].astype(int)  # 取前四个整数值为坐标
                    face = image.crop((box[0], box[1], box[2], box[3]))
                    face_images.append(face)
            cap.release()
            cv2.destroyWindow('camera')
            return face_images