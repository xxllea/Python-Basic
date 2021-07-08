# coding: GB2312
# import re
import os


def rename_file(dir_path):
    dir_name_list = os.listdir(dir_path)
    for dir_name in dir_name_list:

        if dir_name == "�Աȶ�+30":
            string = "_contract_30"
        elif dir_name == "�Աȶ�-30":
            string = "_contract_-30"
        elif dir_name == "�Աȶ�+50":
            string = "_contract_50"
        elif dir_name == "�Աȶ�-50":
            string = "_contract_-50"
        elif dir_name == "����+30":
            string = "_brightness_30"
        elif dir_name == "����-30":
            string = "_brightness_-30"
        elif dir_name == "����+50":
            string = "_brightness_50"
        elif dir_name == "����-50":
            string = "_brightness_-50"
        else:
            dir_name = None

        # �����ļ�·���������ļ���������һ�б�
        file_path = str(dir_path + dir_name)
        file_name_list = os.listdir(file_path)
        for file_name in file_name_list:
            old_file_name = os.path.join(file_path, file_name)

            # ��"2092_contract_30.jpg" ������������> "2092.jpg"��ʽ������
            # new_name = re.sub(string, "", file_name)
            # ����
            # new_name = file_name.replace(string, "")

            # ��"2092.jpg" ������������> "2092_contract_30.jpg"��ʽ������
            new_name = file_name.replace(".jpg", "") + string + ".jpg"

            new_file_name = os.path.join(file_path, new_name)
            os.rename(old_file_name, new_file_name)
        print("[" + dir_name + "]Ŀ¼�������" + str(len(file_name_list)) + "���ļ�����������")

if __name__ == '__main__':
    # ������޸��ļ�Ŀ¼�ĸ�Ŀ¼
    dir_path = "C:/Users/xxllea/OneDrive/����/2/"
    rename_file(dir_path)
