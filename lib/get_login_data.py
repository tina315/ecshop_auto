'''取登录数据'''
import csv
def read_login_data(file_name):
    users = []
    with open(file_name,'r+',encoding='utf-8') as f:
        data = csv.reader(f)
        for user in data:
            users.append(user)
    return users