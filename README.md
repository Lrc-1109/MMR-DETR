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
