import manage_db
import client
import server

class Admin():
    def __init__(self):
        self.C = client.Client()
        self.db = manage_db.Automation_BD()
        self.name = ''

    def Login(self, server_ip, server_port, username, password, key):
        self.name = username
        return self.C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

    ########################################## Admin management section ############# status: implimented ######################
    def Admin_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone):
        report1 = self.db.Insert_admin(username, self.C.Hash(password), first_name, last_name, birth_year, birth_month, birth_day, email, phone)
        report2 = self.db.Insert_admin_workspace(username)
        # self.db.Record_action_log(f'New admin {username} added and his workspace created', username)
        return report1 +'\n'+ report2

    def Admin_del(self, username, password):
        report1 = self.db.Delete_admin(username, self.C.Hash(password))
        report2 = self.db.Delete_admin_workspace(username)
        # self.db.Record_action_log(f'Admin {username} deleted and his workspace removed', username)
        return report1 + '\n' + report2

    def Admin_update(self, username, password, attrib, new_value):
        report1, report2, report3 = '', '', ''
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report1 = self.db.Update_admin(username, self.C.Hash(password), attrib, hash_pass)
            # self.db.Record_action_log(f'{username} password was changed', username)
        elif attrib == 'username':
            report1 = self.db.Update_admin(username, self.C.Hash(password), 'username', new_value)
            report2 = self.db.Update_admin_workspace(username,'owner', new_value)
            report3 = self.db.Update_admin_workspace(new_value,'name', 'ws_auto' + new_value)
            # self.db.Record_action_log(f'{username} username was changed to {new_value}', new_value)
        else:
            report1 = self.db.Update_admin(username, self.C.Hash(password), attrib, new_value)
            # self.db.Record_action_log(f'{username} {attrib} was changed to {new_value}', new_value)

        return report1 + '\n' + report2 + '\n' + report3

    def Admin_find(self, username, password):
        report = self.db.Get_attrib_admin(username, self.C.Hash(password))
        if report == False:
            return f'Admin not found with this username: {username}'
        else:
            return report

    ########################################## User management section ############# status: implemented ######################
    def User_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission):
        report1 = self.db.Insert_user(username, self.C.Hash(password), first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission)
        report2 = self.db.Insert_user_workspace(username)
        # self.db.Record_action_log(f'New user {username} added and his workspace created', username)
        return report1 + '\n' + report2

    def User_del(self, username, password):
        report1 = self.db.Delete_user(username, self.C.Hash(password))
        report2 = self.db.Delete_user_workspace(username)
        # self.db.Record_action_log(f'User {username} deleted and his workspace removed', username)
        return report1 + '\n' + report2

    def User_update(self, username, password, attrib, new_value):
        report1, report2, report3 = '', '', ''
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report1 = self.db.Update_user(username, self.C.Hash(password), attrib, hash_pass)
            # self.db.Record_action_log(f'{username} password was changed', username)
        elif attrib == 'username':
            report1 = self.db.Update_user(username, self.C.Hash(password), 'username', new_value)
            report2 = self.db.Update_user_workspace(username,'owner', new_value)
            report3 = self.db.Update_user_workspace(new_value,'name', 'ws_auto' + new_value)
            # self.db.Record_action_log(f'{username} username was changed to {new_value}', new_value)
        else:
            report1 = self.db.Update_user(username, self.C.Hash(password), attrib, new_value)
            # self.db.Record_action_log(f'{username} {attrib} was changed to {new_value}', new_value)

        return report1 + '\n' + report2 + '\n' + report3

    def User_find(self, username, password):
        report = self.db.Get_attrib_user(username, self.C.Hash(password))
        if report == False:
            return f'User not found with this username: {username}'
        else:
            return report

    ########################################## Server management section ############# status: implemented ######################
    def Server_add(self, hostname, password, domain, ip, port):
        report = self.db.Insert_server(hostname, self.C.Hash(password), domain, ip, port)
        # self.db.Record_action_log(f'New server with hostname: {hostname} and ip/port: {ip}:{port} added', hostname)
        return report

    def Server_del(self, hostname, password):
        report = self.db.Delete_server(hostname, self.C.Hash(password))
        # self.db.Record_action_log(f'Server with hostname: {hostname} and ip/port: {ip}:{port} deleted', hostname)
        return report

    def Server_update(self, hostname, password, attrib, new_value):
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report = self.db.Update_server(hostname, self.C.Hash(password), attrib, hash_pass)
            # self.db.Record_action_log(f'{hostname}:server password was changed', hostname)
        else:
            report = self.db.Update_server(hostname, self.C.Hash(password), attrib, new_value)
            # self.db.Record_action_log(f'{hostname}:server {attrib} was changed to {new_value}', new_value)
        return report

    def Server_find(self, hostname, password):
        report = self.db.Get_attrib_server(hostname, self.C.Hash(password))
        if report == False:
            return f'Server not found with this hostname: {hostname}'
        else:
            return report

    def Start_server(self, hostname, password, ip, port):
        report = self.db.Get_attrib_server(hostname, self.C.Hash(password)) # authenticate server
        if report == False: # if authentication operation was failed, server return False and run_server_form.py can handle it.
            # self.db.Record_action_log(f'{hostname}:server {ip}:{port} had problem for running', hostname)
            return report
        else:
            # self.db.Record_action_log(f'{hostname}:server was running with {ip}:{port}', hostname)
            S = server.Server(ip, port)
            return S.Run_Server() # if ip/port cannot bind to server, server return "internal error" and run_server_form can handle it.

    ########################################## Admin workspace management section ############# status: implemented ######################
    def Admin_workspace_add(self, username):
        report = self.db.Insert_admin_workspace(username)
        return report

    def Admin_workspace_del(self, username):
        report = self.db.Delete_admin_workspace(username)
        return report

    def Admin_workspace_update(self, username, attrib, new_value):
        report = self.db.Update_admin_workspace(username, attrib, new_value)
        return report

    def Admin_workspace_find(self, username):
        report = self.db.Get_attrib_admin_workspace(username)
        if report == False:
            return f'Workspace not found for this username: {username}'
        else:
            return report

    ########################################## User workspace management section ############# status: implemented ######################
    def User_workspace_add(self, username):
        report = self.db.Insert_user_workspace(username)
        return report

    def User_workspace_del(self, username):
        report = self.db.Delete_user_workspace(username)
        return report

    def User_workspace_update(self, username, attrib, new_value):
        report = self.db.Update_user_workspace(username, attrib, new_value)
        return report

    def User_workspace_find(self, username):
        report = self.db.Get_attrib_user_workspace(username)
        if report == False:
            return f'Workspace not found for this username: {username}'
        else:
            return report

    ########################################## Script management section ############# status: implement 70% ######################
    def Launch_script(self, script_name):
        pass
    def Edit_script(self, script_name, path):
        pass
    def Create_script(self, script_name, path, usability):
        report = self.db.Insert_script(script_name, path, usability)
        # self.db.Record_action_log(report, script_name)
        return report

    def Del_script(self, script_name):
        report = self.db.Delete_script(script_name)
        # self.db.Record_action_log(report, script_name)
        return report

    def Up_script(self, script_name, attrib, new_value):
        report = self.db.Update_script(script_name, attrib, new_value)
        # self.db.Record_action_log(report, script_name)
        return report

    def Find_script(self,script_name):
        report = self.db.Get_attrib_script(script_name)
        return report

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

if __name__ == "__main__":
    A = Admin()
    # print(A.Admin_add('maxi', '1234', 'max', 'G', '1994', '8', '5', 'maxi@gmail.com', '0933'))
    # print(A.Admin_update('MAXI', '123', 'phone', '0954'))
    # print(A.Admin_del('alex2', '1234'))
    # print(A.Admin_find('MAXI', '123'))

    # print(A.All_login_log())
    # print(A.Login_log('username', 'alex2'))
    # print(A.All_action_log())
    # print(A.Action_log('username', 'mixtape'))

    # print(A.User_add('Bob', '123', 'bob', 'pat', '1989', '3', '1', 'bob@gmail.com', '0905', False))
    # print(A.User_update('JAX', '12345', 'phone', '0987'))
    # print(A.User_del('Bob', '123'))
    # print(A.User_find('Jax', '123'))

    # print(A.Server_add('automation', '123456', 'automation.com', '127.0.0.1', 4444))
    # print(A.Server_update('automation', '123', 'password', '123456'))
    # print(A.Server_del('automation', '123456'))
    # print(A.Server_find('automation', '123456'))
    # print(A.Start_server('automation', '123456', '127.0.0.1', 4444))

    # print(A.Create_script('set-ntp', "/home/mehrdad/Documents/my-git/automation/automation_scripts/", "Set ntp protocol"))
    # print(A.Del_script('get-interface.py'))
    # print(A.Up_script('get-interface.py', 'path', "/home/mehrdad/Documents/my-git/automation/automation_scripts/"))
    # print(A.Find_script('get-interface.py'))

    # print(A.Admin_workspace_add('mixtape'))
    # print(A.User_workspace_add('Jax'))
    # print(A.Admin_workspace_update('mixtape', '12345', 'owner', 'Mixtape'))
    # print(A.User_workspace_update('Jax', '1234', 'owner', 'JAX'))
    # print(A.Admin_workspace_del('mixtape', '12345'))
    # print(A.User_workspace_del('Jax', '1234'))
    # print(A.Admin_workspace_find('mixtape'))
    # print(A.User_workspace_find('Jax'))