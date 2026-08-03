import math

def calculate_average(data_list):
    if not data_list:
        return 0
    return sum(data_list) / len(data_list)

def calculate_max_min(data_list):
    if not data_list:
        return 0 ,0
    return max(data_list) , min(data_list)

def calculate_std(data_list):
    if not data_list:
        return 0
    avg = calculate_average(data_list)
    #标准差：每个数值与均值差值的平方求和
    square_sum = sum((x-avg) **2 for x in data_list)
    variance = square_sum / len(data_list)
    std = math.sqrt(variance)
    return std


#=====读写函数======
def load_data(file_path):
    # 读取文件，每行数字转为列表
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data_list = []
        for line in lines:
            line = line.strip()
            if line:
                data_list.append(float(line))
        return data_list

    except FileNotFoundError:
        print(f"警告：文件{file_path}不存在")
        return []
    except ValueError:
        print(f"警告：文件内存在无法转换为数字的内容")
        return []

def save_data(file_path, content):
    #写入结果文件
    with open(file_path, "w", encoding ="utf-8")as f:
        f.write(content)

    print(f"结果已保存至{file_path}")




#=======程序入口========
if __name__ == "__main__":
    # 分段测试
    print("=====单元测试：caculate_average =====")

    test_case_avg =[
        [],
        [9,6],
        [12,45,64,42,95,15],
        [-1.5,4.6,-4.6]
    ]

    for case in test_case_avg:
        avg = calculate_average(case)
        print(f"输入{case} - 平均值:{avg:.2f}")

    print("=====单元测试：caculate_max_min ====")

    test_case_mm =[
        [],
        [9,6],
        [12,45,64,42,95,15],
        [-1.5,4.6,-4.6]
    ]

    for case in test_case_mm:
        max_v, min_v = calculate_max_min(case)
        print(f"输入{case} - 最大值：{max_v:.2f}, 最小值：{min_v: .2f}")

    print("=======单元测试：caculate_std =====")

    test_case_std =[
        [],
        [9,6],
        [12,45,64,42,95,15],
        [-1.5,4.6,-4.6]
    ]

    for case in test_case_std:
        std_v = calculate_std(case)
        print(f"输入{case} - 标准差：{std_v: .2f}")

    print("\n======单元测试： 文件读写测试======")
    # 测试1：故意读取不存在的文件
    data_fail = load_data("not_exist.txt")

    print("不存在的文件读取结果：", data_fail)

    # 测试2：正常业务流程
    data = load_data("sensor_data.txt")
    if data:
        avg = calculate_average(data)
        max_v, min_v = calculate_max_min(data)
        std_v = calculate_std(data)
        output_text = (
            f"原始数据: {data}\n"
            f"平均值： {avg: .2f}\n"
            f"最大值： {max_v: .2f}\n"
            f"最小值: {min_v: .2f}\n"
            f"总体标准差: {std_v: .2f}\n"
        )

        save_data("stats_result.txt", output_text)

    else:
        print("未加载到有效数据， 跳过计算！")









    
