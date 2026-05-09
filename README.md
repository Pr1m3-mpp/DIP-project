# DIP-project
## 数据准备

本实验使用的图片数据已打包为 `DIP_data.zip`，请从百度网盘下载并解压到项目根目录。

- **下载链接**：https://pan.baidu.com/s/1F6RnlpcQKTiW60X_LCIyJQ?pwd=wnjw  
- **提取码**：`wnjw`

文件结构：
```text
DIP_data.zip
├── raw_data/                       # 原始的300张图片
├── processed_data/                 # 传统图像预处理后的300张图片
├── data/                           # YOLO 格式文件
│   ├── images/                     # 划分后的图片
│   │   ├── test/                   # 测试集30张图片
│   │   ├── train/                  # 训练集240张图片
│   │   └── val/                    # 验证集30张图片
│   └── labels/                     # LabelImg 标注后的.txt文本
│       ├── test/                   # 测试集.txt文本
│       ├── train/                  # 训练集.txt文本
│       └── val/                    # 验证集.txt文本
└── yolov5/                         # 训练和测试后的YOLOv5s 框架
    ├── data/
    │   └── MyDataSpec.yaml/        # 修改nc后的YOLO 配置文件
    ├── models/
    │   └── MyModelSpec.yaml/       # 修改nc和names后的YOLO 配置文件
    └── runs/
        ├── train/                  # 训练结果
        └── detect/                 # 测试结果
