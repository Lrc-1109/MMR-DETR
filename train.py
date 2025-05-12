import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('ultralytics/cfg/models/rt-detr/MMS-DETR.yaml')
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=150,
                batch=8,
                device='0',
                project='runs/train',
                name='exp',
                )