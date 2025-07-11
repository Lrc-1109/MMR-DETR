import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR(r'G:\lrc\RDD runs\detr\weights\best.pt')
    model.val(data='dataset/data.yaml',
              split='test', 
              imgsz=640,
              batch=2,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )
