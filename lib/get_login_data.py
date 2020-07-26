'''取登录数据'''
import csv

class ReadCsv():
    '''读取csv数据'''
    def read_login_data(self,file_name):
        '''读取用户登录数据'''
        users = []
        with open(file_name,'r+',encoding='utf-8') as f:
            data = csv.reader(f)
            for user in data:
                users.append(user)
        return users

    def read_admin_data(self,file_name):
        '''读取后台管理员登录数据'''
        users = []
        with open(file_name, 'r+', encoding='utf-8') as f:
            data = csv.reader(f)
            for user in data:
                users.append(user)
        return users

    def read_addr_data(self,file_name):
        '''读取后台管理员登录数据'''
        addrs = []
        with open(file_name, 'r+', encoding='utf-8') as f:
            data = csv.reader(f)
            for addr in data:
                addrs.append(addr)
        return addrs
