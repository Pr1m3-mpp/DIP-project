import os
import glob
import shutil
from sklearn.model_selection import train_test_split


def create_yolo_structure(base_path="data"):
    """创建 YOLO 要求的标准文件夹结构"""
    folders = [
        f"{base_path}/images/train", f"{base_path}/images/val", f"{base_path}/images/test",
        f"{base_path}/labels/train", f"{base_path}/labels/val", f"{base_path}/labels/test"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("标准目录结构创建完毕！")


def split_and_copy_data(input_dir="processed_data", output_dir="data"):
    """按 8:1:1 划分数据集并复制图片"""
    # 获取所有图片路径
    all_images = glob.glob(os.path.join(input_dir, "*.*"))
    if len(all_images) == 0:
        print("未找到图片，请检查 processed_data 文件夹！")
        return

    print(f"共找到 {len(all_images)} 张图片，开始划分...")

    # 第一次划分：分出 80% 作为训练集，剩下 20% 作为临时集
    train_imgs, temp_imgs = train_test_split(all_images, test_size=0.2, random_state=42)
    # 第二次划分：将剩下的 20% 对半分为验证集 (10%) 和测试集 (10%)
    val_imgs, test_imgs = train_test_split(temp_imgs, test_size=0.5, random_state=42)

    # 定义复制动作的辅助函数
    def copy_files(file_list, target_subfolder):
        target_path = os.path.join(output_dir, "images", target_subfolder)
        for f in file_list:
            shutil.copy(f, target_path)

    # 执行复制
    copy_files(train_imgs, "train")
    copy_files(val_imgs, "val")
    copy_files(test_imgs, "test")

    print(f"数据集划分完成！")
    print(f"训练集 (Train): {len(train_imgs)} 张")
    print(f"验证集 (Val): {len(val_imgs)} 张")
    print(f"测试集 (Test): {len(test_imgs)} 张")


if __name__ == "__main__":
    # 1. 创建文件夹
    create_yolo_structure()
    # 2. 划分并复制图片
    split_and_copy_data()