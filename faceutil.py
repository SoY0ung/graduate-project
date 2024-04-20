import cv2
import numpy as np
import os
from PIL import Image, ImageFont, ImageDraw

from mtcnn.detector import detect_faces
from facenet.network import Facenet

# Recommended threshold 0.92

class FaceUtil:

    face_database = {}

    def __init__(self, database_path, **kwargs):
        self.face_database = self.create_face_database(database_path)


    def get_cam_faces(self, countdown = 30):
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
            
    def get_img_faces(self, img):
        bounding_boxes, _ = detect_faces(img)
        # 裁剪检测到的人脸
        face_images = []

        if bounding_boxes is not None:
            for box in bounding_boxes:
                box = box[:4].astype(int)  # 取前四个整数值为坐标
                face = img.crop((box[0], box[1], box[2], box[3]))
                face_images.append(face)
        return face_images

    # 获取人脸图片的距离
    def get_distance(self, faceImg_1, faceImg_2, debug=False):
        model = Facenet(detail=debug)
        dist = model.detect_image(faceImg_1, faceImg_2, show=debug).item()
        print(dist)
        return dist

    # 获取人脸图片的特征向量
    def get_feature(self, faceImg, debug=False):
        model = Facenet(detail=debug)
        face_embedding = model.generate_feature_vector(faceImg)
        return face_embedding
    
    # 获取特征向量的距离
    def get_feature_distance(self, feature_1, feature_2):
        return np.linalg.norm(feature_1 - feature_2, axis=1).item()

    # 为本地人脸库生成特征向量
    def create_face_database(self, folder_path, debug=False):
        model = Facenet(detail=debug)
        face_embeddings = {}
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                name = filename.split('.')[0]  # 假设文件名即人名
                image_path = os.path.join(folder_path, filename)
                image = Image.open(image_path)
                face_embedding = model.generate_feature_vector(image)
                face_embeddings[name] = face_embedding
        return face_embeddings
    
    # 在本地人脸库中找到最匹配的人脸
    def recognize_face(self, input_face):
        """
        Return Possible_Name, distance
        """
        input_embedding = self.get_feature(input_face)
        # 初始化最小距离为非常大的数，用于找到最小值
        min_distance = float('inf')
        identity = None
        # 遍历数据库中的每个人脸特征向量
        for name, db_embedding in self.face_database.items():
            distance = self.get_feature_distance(input_embedding, db_embedding)
            if distance < min_distance:
                min_distance = distance
                identity = name
        return identity, min_distance

    