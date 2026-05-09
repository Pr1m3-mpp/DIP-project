import cv2
import numpy as np
import os
import glob


def process_images(input_dir, output_dir, target_size=(512, 512), gamma=0.5, blur_ksize=3):
    """
    对极暗图像进行批量预处理
    :param input_dir: 原始图片文件夹路径
    :param output_dir: 处理后图片保存路径
    :param target_size: 统一缩放的尺寸
    :param gamma: 伽马变换参数 (小于1提亮暗部)
    :param blur_ksize: 中值滤波核大小 (必须是奇数)
    """
    # 如果输出文件夹不存在，则自动创建
    os.makedirs(output_dir, exist_ok=True)

    # 支持多种常见图片格式
    extensions = ('*.jpg', '*.jpeg', '*.png')
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(input_dir, ext)))

    if not image_paths:
        print(f"在 {input_dir} 中没有找到图片，请检查路径！")
        return

    print(f"找到 {len(image_paths)} 张图片，开始处理...")

    success_count = 0
    for img_path in image_paths:
        img_name = os.path.basename(img_path)

        # 1. 读取图片 (cv2 读取的格式默认为 BGR)
        img = cv2.imread(img_path)
        if img is None:
            print(f"警告: 无法读取图片 {img_name}")
            continue

        # 2. 统一尺寸 (Resize)
        img_resized = cv2.resize(img, target_size)

        # 3. 灰度变换：幂律（伽马）变换
        # 将像素值归一化到 [0, 1] 区间，应用公式 s = c * r^gamma (此处设 c=1)
        img_normalized = img_resized / 255.0
        img_gamma = np.power(img_normalized, gamma)
        # 将像素值还原回 [0, 255] 并转为 uint8 类型
        img_gamma = np.uint8(img_gamma * 255)

        # 4. 空间域滤波：中值滤波
        # 去除提亮后暴露出的传感器高频噪点，同时保护目标边缘不被模糊
        img_filtered = cv2.medianBlur(img_gamma, blur_ksize)

        # 5. 保存处理后的图片
        save_path = os.path.join(output_dir, img_name)
        cv2.imwrite(save_path, img_filtered)
        success_count += 1

    print(f"预处理完成！成功处理并保存了 {success_count} 张图片到 '{output_dir}' 文件夹。")


if __name__ == "__main__":
    # 配置输入和输出文件夹
    RAW_DATA_DIR = 'raw_data'
    PROCESSED_DATA_DIR = 'processed_data'

    # 执行处理逻辑
    process_images(
        input_dir=RAW_DATA_DIR,
        output_dir=PROCESSED_DATA_DIR,
        target_size=(512, 512),
        gamma=0.5,  # 伽马值设为 0.5，显著提亮暗部
        blur_ksize=3  # 使用 3x3 的中值滤波核
    )