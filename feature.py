import faceutil
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

camface = faceutil.get_cam_faces()
if len(camface) > 0:
    # plt.imshow(np.array(camface[0]))
    # plt.show()
    camface = camface[0]
else:
    print("No face detected!")

localImg = input('Input img path:')
localImg = Image.open(localImg)
localface = faceutil.get_img_faces(localImg)

if len(localface) > 0:
    # plt.imshow(np.array(localface[0]))
    # plt.show()
    localface = localface[0]
else:
    print("No face detected!")

faceutil.get_distance(camface, localface, debug=True)

