import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR
from cv2 import imread


if __name__ == '__main__':
    model = RTDETR(r'G:\lrc\RDD runs\detr\weights\best.pt') # select your model.pt path
    model.predict(source=r'G:\lrc\RDD\1',
                  conf=0.3,
                  project=r'G:\lrc\RDD',
                  name='detr',
                  
                  save=True,

                  )
