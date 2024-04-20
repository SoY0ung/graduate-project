from PIL import Image

from mtcnn import detector
from facenet.network import Facenet
# Recommend threshold 0.92

def detect_faces(img):
    bounding_boxes, _ = detector.detect_faces(img)
    # 裁剪检测到的人脸
    face_images = []

    if bounding_boxes is not None:
        for box in bounding_boxes:
            box = box[:4].astype(int)  # 取前四个整数值为坐标
            face = img.crop((box[0], box[1], box[2], box[3]))
            face_images.append(face)
    return face_images


def face_distance(image_1, image_2, debug=False):
    model = Facenet(detail=debug)
        
    try:
        image_1 = detect_faces(image_1)
    except:
        print('Error when processing image 1!')

    try:
        image_2 = detect_faces(image_2)
    except:
        print('Error when processing image 2!')
    
    if len(image_1) > 0 and len(image_2) > 0:
        probability = model.detect_image(image_1[0], image_2[0], show=False)
        print(probability)
    else:
        print("No face detected!")
        
    return probability
