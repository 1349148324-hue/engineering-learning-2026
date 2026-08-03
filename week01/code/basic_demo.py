#!/usr/bin/env python3
# DAY1 基础练习：文件读写与简单计算
# 存放路径：week01/code/basic_demo.py

def calculate_average(data_list):
    """计算列表平均值"""
    if not data_list:
        return 0
    return sum(data_list) / len(data_list)


def save_data(file_path, data):
    """将数据写入文本文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(data))


def load_data(file_path):
    """读取文本文件数据"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    nums = [12, 34, 45, 67, 89]
    avg = calculate_average(nums)
    print(f"数据集 {nums} 的平均值：{avg:.2f}")

    save_data("result.txt", avg)
    res = load_data("result.txt")
    print("从文件读取结果：", res)