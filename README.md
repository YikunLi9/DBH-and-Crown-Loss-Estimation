# Tree DBH Measurement and Crown Loss Estimation Using iPhone LiDAR and Computer Vision

This repository contains Python scripts, datasets, and SQL files for implementing and training models to measure Diameter at Breast Height (DBH) using LiDAR data and estimate crown loss using computer vision techniques.

## Overview

This project was developed as part of a study aimed at enhancing tree surveying methods by utilizing affordable technology such as the iPhone's LiDAR sensor and camera. The main goals are to improve the accuracy of DBH measurement and the efficiency of crown loss estimation, making these methods more accessible and cost-effective.

## Contents

```
├── DBH mearsurement
│   ├── point cloud model: Directory to store example point cloud
│   │   ├── 1.las
│   │   ├── 2.las
│   │   ├── 3.las
│   │   └── 4.las
│   └── pre-processing&LM.py: Python script to calculate the DBH
├── crown loss estimation
│   └── dataset
│       └── crownloss.v1i.yolov5-obb: Dataset in the formt of yolov5
│           ├── data.yaml
│           ├── README.roboflow.txt
│           ├── test
│           ├── valid
│           └── train
└── database
    └── database_setup.sql: Script to build such database
```

## DBH Measurement

The DBH measurement script uses point cloud data captured by the iPhone's LiDAR sensor to calculate the tree's diameter at breast height. The script processes the point cloud data to extract the trunk profile, then applies circle fitting algorithms to determine the DBH.

### Requirements

- Python 3.x
- `numpy`
- `scipy`
- `matplotlib`
- `argparse`

### Usage

1. Capture point cloud data using an iPhone with LiDAR.

2. Transfer the data to your local machine.

3. Run the `dbh_measurement.py` script:

   ```
   python pre-processing&LM.py /path/to/your/file.las
   ```



## Crown Loss Estimation

This module trains a YOLO-based model to detect and estimate crown loss using images captured by the iPhone camera. The model aims to provide a more accurate and efficient alternative to manual visual assessments.

### Requirements

- Python 3.x
- `Tensorflow`
- `numpy`
- `pandas`
- `cv2`
- `YOLOv5`

### Dataset

The dataset used for training is included in the `crown loss estimation/dataset/` directory. It contains images of trees with annotated crown loss levels.

### Training the Model

To train the crown loss detection model, move dataset to yolo directory and run:

```
python train.py --data dataset.yaml --cfg yolov5.yaml --weights yolov5s.pt --epochs 100
```



## Database Setup

The `database_setup.sql` file contains the necessary SQL commands to create a database for storing tree measurement data. This database will keep records of each tree's DBH and crown loss over time, enabling tracking and analysis of tree health trends.

### Setup Instructions

1. Install a SQL database server (e.g., MySQL, PostgreSQL).

2. Run the `database_setup.sql` script to create the necessary tables:

   ```
   mysql -u username -p < database_setup.sql
   ```



## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.