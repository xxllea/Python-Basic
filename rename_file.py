# coding: GB2312
# import re
import os


def rename_file(dir_path):
    dir_name_list = os.listdir(dir_path)
    for dir_name in dir_name_list:

        if dir_name == "对比度+30":
            string = "_contract_30"
        elif dir_name == "对比度-30":
            string = "_contract_-30"
        elif dir_name == "对比度+50":
            string = "_contract_50"
        elif dir_name == "对比度-50":
            string = "_contract_-50"
        elif dir_name == "亮度+30":
            string = "_brightness_30"
        elif dir_name == "亮度-30":
            string = "_brightness_-30"
        elif dir_name == "亮度+50":
            string = "_brightness_50"
        elif dir_name == "亮度-50":
            string = "_brightness_-50"
        else:
            dir_name = None

        # 根据文件路径下所有文件名，生成一列表
        file_path = str(dir_path + dir_name)
        file_name_list = os.listdir(file_path)
        for file_name in file_name_list:
            old_file_name = os.path.join(file_path, file_name)

            # 将"2092_contract_30.jpg" ——————> "2092.jpg"形式的数据
            # new_name = re.sub(string, "", file_name)
            # 或者
            # new_name = file_name.replace(string, "")

            # 将"2092.jpg" ——————> "2092_contract_30.jpg"形式的数据
            new_name = file_name.replace(".jpg", "") + string + ".jpg"

            new_file_name = os.path.join(file_path, new_name)
            os.rename(old_file_name, new_file_name)
        print("[" + dir_name + "]目录下已完成" + str(len(file_name_list)) + "个文件批量重命名")

if __name__ == '__main__':
    # 输入待修改文件目录的父目录
    dir_path = "C:/Users/xxllea/OneDrive/桌面/2/"
    rename_file(dir_path)
