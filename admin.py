import manage_db
import client

class Admin():
    def __init__(self):
        self.C = client.Client()
        self.db = manage_db.Automation_BD()

    def Login(self, server_ip, server_port, username, password, key):
        C = client.Client()
        return C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

    ########################################## Admin management section ############# status: implimented ######################
    def Admin_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone):
        report = self.db.Insert_admin(username, self.C.Hash(password), first_name, last_name, birth_year, birth_month, birth_day, email, phone)
        return report

    def Admin_del(self, username, password):
        report = self.db.Delete_admin(username, self.C.Hash(password))
        return report

    def Admin_update(self, username, password, attrib, new_value):
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report = self.db.Update_admin(username, self.C.Hash(password), attrib, hash_pass)
        else:
            report = self.db.Update_admin(username, self.C.Hash(password), attrib, new_value)
        return report

    def Admin_find(self, username, password):
        report = self.db.Get_attrib_admin(username, self.C.Hash(password))
        if report == False:
            return f'Admin not found with this username: {username}'
        else:
            return report

    ########################################## User management section ############# status: implemented ######################
    def User_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission):
        report = self.db.Insert_user(username, self.C.Hash(password), first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission)
        return report

    def User_del(self, username, password):
        report = self.db.Delete_user(username, self.C.Hash(password))
        return report

    def User_update(self, username, password, attrib, new_value):
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report = self.db.Update_user(username, self.C.Hash(password), attrib, hash_pass)
        else:
            report = self.db.Update_user(username, self.C.Hash(password), attrib, new_value)
        return report

    def User_find(self, username, password):
        report = self.db.Get_attrib_user(username, self.C.Hash(password))
        if report == False:
            return f'User not found with this username: {username}'
        else:
            return report

    ########################################## Server management section ############# status: implemented ######################
    def Server_add(self, hostname, password, domain, ip, port):
        report = self.db.Insert_server(hostname, self.C.Hash(password), domain, ip, port)
        return report

    def Server_del(self, hostname, password):
        report = self.db.Delete_server(hostname, self.C.Hash(password))
        return report

    def Server_update(self, hostname, password, attrib, new_value):
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report = self.db.Update_server(hostname, self.C.Hash(password), attrib, hash_pass)
        else:
            report = self.db.Update_server(hostname, self.C.Hash(password), attrib, new_value)
        return report

    def Server_find(self, hostname, password):
        report = self.db.Get_attrib_server(hostname, self.C.Hash(password))
        if report == False:
            return f'Server not found with this hostname: {hostname}'
        else:
            return report

    ########################################## Script management section ############# status: none ######################
    def Run_script(self, script_name):
        pass
    def Create_script(self, script_name, path):
        pass
    def Edit_script(self, script_name, path):
        pass
    def Del_script(self, script_name, path):
        pass

    ########################################## Log management section ############# status: implemented ######################
    def All_login_log(self):
        log = {}
        log_list = []
        for dict in self.db.Show_all_login_log():
            log['date'] = list(dict.values())[1] + '-' + list(dict.values())[2] + '-' + list(dict.values())[3] + ' ' + \
                          list(dict.values())[4] + ':' + list(dict.values())[5] + ':' + list(dict.values())[6]
            log['content'] = list(dict.values())[7] + ':'
            log['user'] = list(dict.values())[8]
            log['workspace'] = list(dict.values())[9]
            log_list.append(log)
        return log_list

    def Login_log(self, attrib, value):
        log = {}
        log_list = []
        for dict in self.db.Show_login_log(attrib, value):
            log['date'] = list(dict.values())[1] + '-' + list(dict.values())[2] + '-' + list(dict.values())[3] + ' ' + \
                          list(dict.values())[4] + ':' + list(dict.values())[5] + ':' + list(dict.values())[6]
            log['content'] = list(dict.values())[7] + ':'
            log['user'] = list(dict.values())[8]
            log['workspace'] = list(dict.values())[9]
            log_list.append(log)
        return log_list

    def All_action_log(self):
        log = {}
        log_list = []
        for dict in self.db.Show_all_action_log():
            log['date'] = list(dict.values())[1] + '-' + list(dict.values())[2] + '-' + list(dict.values())[3] + ' ' + \
                          list(dict.values())[4] + ':' + list(dict.values())[5] + ':' + list(dict.values())[6]
            log['content'] = list(dict.values())[7] + ':'
            log['user'] = list(dict.values())[8]
            log['workspace'] = list(dict.values())[9]
            log_list.append(log)
        return log_list

    def Action_log(self, attrib, value):
        log = {}
        log_list = []
        for dict in self.db.Show_action_log(attrib, value):
            log['date'] = list(dict.values())[1] + '-' + list(dict.values())[2] + '-' + list(dict.values())[3] + ' ' + \
                          list(dict.values())[4] + ':' + list(dict.values())[5] + ':' + list(dict.values())[6]
            log['content'] = list(dict.values())[7] + ':'
            log['user'] = list(dict.values())[8]
            log['workspace'] = list(dict.values())[9]
            log_list.append(log)
        return log_list

    ########################################## Monitor management section ############# status: none ######################
    def Monitor_server(self):
        pass

    ########################################## SSH management section ############# status: none ######################
    def SSH(self, username, ip_address):
        pass

# if __name__ == "__main__":
#     A = Admin()
    # print(A.Admin_add('alex2', '1234', 'alex', 'D', '1990', '6', '5', 'alex@gmail.com', '0933'))
    # print(A.Admin_update('mixtape', '123', 'password', '12345'))
    # print(A.Admin_del('alex2', '1234'))
    # print(A.Admin_find('alex2', '1234'))

    # print(A.All_login_log())
    # print(A.Login_log('username', 'alex2'))
    # print(A.All_action_log())
    # print(A.Action_log('username', 'mixtape'))

    # print(A.User_add('Jax', '123', 'jack', 'mark', '1987', '1', '1', 'jack@gmail.com', '0935', False))
    # print(A.User_update('Jax', '123', 'password', '1234'))
    # print(A.User_del('Jax', '123'))
    # print(A.User_find('Jax', '123'))

    # print(A.Server_add('automation', '123456', 'automation.com', '127.0.0.1', 4444))
    # print(A.Server_update('automation', '123456', 'ip', '127.0.0.1'))
    # print(A.Server_del('automation', '123456'))
    # print(A.Server_find('automation', '123456'))