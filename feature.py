import faceutil
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def recognize_face(input_face, face_database):
    input_embedding = faceutil.get_feature(input_face)
    # 初始化最小距离为非常大的数，用于找到最小值
    min_distance = float('inf')
    identity = None
    # 遍历数据库中的每个人脸特征向量
    for name, db_embedding in face_database.items():
        distance = faceutil.get_feature_distance(input_embedding, db_embedding)
        if distance < min_distance:
            min_distance = distance
            identity = name
    return identity

database_path = 'database/'
face_database = faceutil.create_face_database(database_path)

camImg = faceutil.get_cam_faces()
if len(camImg) > 0:
    camImg = camImg[0]
else:
    print('No face detected!')

recognized_name = recognize_face(camImg, face_database)
print(f"The recognized face is: {recognized_name}")

