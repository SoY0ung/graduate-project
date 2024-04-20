from cam4cv import detect_cam_faces
import matplotlib.pyplot as plt
import numpy as np

faces = detect_cam_faces()
if len(faces) > 0:
    plt.imshow(np.array(faces[0]))
    plt.show()
else:
    print("No face detected!")


