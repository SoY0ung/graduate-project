import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.backends.cudnn as cudnn

from facenet.utils.utils import preprocess_input, resize_image, show_config
from facenet.nets.facenet import Facenet as facenet


class Facenet(object):
    _defaults = {
        # 模型目录
        "model_path"    : "facenet/model/facenet_mobilenet.pth",
        # 输入的图片维度大小
        "input_shape"   : [160, 160, 3],
        # 主干特征提取网络，此处选用mobilenet
        "backbone"      : "mobilenet",
        # 是否进行不失真的resize
        "letterbox_image"   : True,
        # cuda加速
        "cuda"              : True,
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    #   初始化Facenet
    def __init__(self, detail=False, **kwargs):
        self.detail = detail
        self.__dict__.update(self._defaults)
        for name, value in kwargs.items():
            setattr(self, name, value)

        self.generate(detail)
        if detail:
            show_config(**self._defaults)
        
    def generate(self, detail):
        #   载入模型与权值
        if detail:
            print('Loading weights into state dict...')
        device      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.net    = facenet(backbone=self.backbone, mode="predict").eval()
        self.net.load_state_dict(torch.load(self.model_path, map_location=device), strict=False)
        if detail:
            print('{} model loaded.'.format(self.model_path))

        if self.cuda:
            self.net = torch.nn.DataParallel(self.net)
            cudnn.benchmark = True
            self.net = self.net.cuda()
    
    #   检测图片
    def detect_image(self, image_1, image_2, show=True):
        #   图片预处理，归一化
        with torch.no_grad():
            image_1 = resize_image(image_1, [self.input_shape[1], self.input_shape[0]], letterbox_image=self.letterbox_image)
            image_2 = resize_image(image_2, [self.input_shape[1], self.input_shape[0]], letterbox_image=self.letterbox_image)
            
            photo_1 = torch.from_numpy(np.expand_dims(np.transpose(preprocess_input(np.array(image_1, np.float32)), (2, 0, 1)), 0))
            photo_2 = torch.from_numpy(np.expand_dims(np.transpose(preprocess_input(np.array(image_2, np.float32)), (2, 0, 1)), 0))
            
            if self.cuda:
                photo_1 = photo_1.cuda()
                photo_2 = photo_2.cuda()
                
            #   传入网络进行预测
            output1 = self.net(photo_1).cpu().numpy()
            output2 = self.net(photo_2).cpu().numpy()

            #   计算两向量之间的距离
            l1 = np.linalg.norm(output1 - output2, axis=1)
        
        if show:
            plt.subplot(1, 2, 1)
            plt.imshow(np.array(image_1))

            plt.subplot(1, 2, 2)
            plt.imshow(np.array(image_2))
            plt.text(-12, -12, 'Distance:%.3f' % l1, ha='center', va= 'bottom',fontsize=11)
            plt.show()
        return l1
