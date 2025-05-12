# MMS-DETR
The implementation code for MMS-DETR. The .pth file contains the main training weights.

# Datasets
This is the code base for a paper submitted to IEEE TIM. This paper presents a novel road damage detection model based on improved RT-DETR, implemented on three publicly available datasets for experiments. 
If you find the code useful, please cite the following paper.

# Highlights



#  Usage
# Environment 
The code is developed under the following configurations:Ubuntu 18.04 Linux operating system, configured with three NVIDIA GeForce RTX 2080Ti GPUs, each with 11GB of memory.
1.Install conda and create a conda environment
  $ conda create -n MMS-DETR
  $ conda activate MMS-DETR
  $ pip install -r requirements.txt
# Training
  $ CUDA VISIBLE DEVICEs=0 python train.py
# Test
  $ python detect.py
# Val
  $ python val.py
# Datsets
The RDD2022, UAPD, and UAV-PDD2023 datasets can be downloaded with:
RDD2022:https://github.com/sekilab/RoadDamageDetector
UAPD:https://drive.google.com/file/d/16rAC8E52oUAWZ4YXb3O3_25qMUTRhdfV/view?usp=sharing
UAV-PDD2023:https://zenodo.org/records/8429208
Many thanks to the following Crowdsensing-based Road Damage Detection Challenge (CRDDC'2022) and the following papers for providing datasets.
J. Zhu, J. Zhong, T. Ma, X. Huang, W. Zhang, and Y. Zhou, “Pavement distress detection using convolutional neural networks with images captured via UAV,” Autom. Constr., vol. 133, Jan. 2022, Art. no. 103991.
H. Yan, J. Zhang, “UAV-PDD2023: a benchmark dataset for pavement distress detection based on UAV images,” Data Brief, vol. 51, Dec. 2023, Art. no. 109692.
