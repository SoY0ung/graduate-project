from PIL import Image

from mtcnn import detector
from facenet.network import Facenet
# Recommend threshold 0.92

def detect_faces(image_path):
    img = Image.open(image_path)
    bounding_boxes, _ = detector.detect_faces(img)
    # 裁剪检测到的人脸
    face_images = []

    if bounding_boxes is not None:
        for box in bounding_boxes:
            box = box[:4].astype(int)  # 取前四个整数值为坐标
            face = img.crop((box[0], box[1], box[2], box[3]))
            face_images.append(face)
    return face_images


if __name__ == "__main__":
    model = Facenet()
        
    while True:
        image_1 = input('Input image_1 filename:')
        # image_1 = 'img/zq1.jpg'
        try:
            image_1 = detect_faces(image_1)
        except:
            print('Image_1 Open Error! Try again!')
            continue

        image_2 = input('Input image_2 filename:')
        try:
            image_2 = detect_faces(image_2)
        except:
            print('Image_2 Open Error! Try again!')
            continue
        
        if len(image_1) > 0 and len(image_2) > 0:
            probability = model.detect_image(image_1[0], image_2[0])
            print(probability)
        else:
            print("No face detected!")
