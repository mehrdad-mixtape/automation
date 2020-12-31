import manage_db, client, server, os

class Admin():
    def __init__(self):
        self.C = client.Client()
        self.db = manage_db.Automation_BD()

    def Login(self, server_ip, server_port, username, password, key):
        if self.C.Connect_to_server(server_ip, server_port) == 'C_F':
            return 'C_F'
        else:
            if self.C.Authenticate_to_server(username, password, key) == 'A_S':
                return 'A_S'
            else:
                return 'A_F'

    def Send_msg(self, msg):
        self.C.Send_Message(self.C.client_socket, msg)

    def Send_B_msg(self, msg):
        self.C.Send_Big_Message(self.C.client_socket, msg)

    def Recv_msg(self):
        return self.C.Receive_Message(self.C.client_socket)

    def Recv_B_msg(self):
        return self.C.Receive_Big_Message(self.C.client_socket)

    ########################################## Admin management section ############# status: implimented ######################
    def Admin_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone):
        msg = 'new ' + 'admin ' + f"{username} {self.C.Hash(password)} {first_name} {last_name} {birth_year} {birth_month} {birth_day} {email} {phone}"
        self.Send_msg(msg)

    def Admin_del(self, username, password):
        msg = 'del ' + 'admin ' + f"{username} {self.C.Hash(password)}"
        self.Send_msg(msg)
        while True:  # I try to get logs from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

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
        msg = 'new ' + 'user ' + f"{username} {self.C.Hash(password)} {first_name} {last_name} {birth_year} {birth_month} {birth_day} {email} {phone} {permission}"
        self.Send_msg(msg)

    def User_del(self, username, password):
        msg = 'del ' + 'user ' + f"{username} {self.C.Hash(password)}"
        self.Send_msg(msg)
        while True:  # I try to get logs from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

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
        msg = 'new ' + 'server ' + f"{hostname} {self.C.Hash(password)} {domain} {ip} {port}"
        self.Send_msg(msg)

    def Server_del(self, hostname, password):
        msg = 'del ' + 'server ' + f"{hostname} {self.C.Hash(password)}"
        self.Send_msg(msg)
        while True:  # I try to get logs from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

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

    ########################################## Script management section ############# status: implement 100% ######################
    def Create_script(self, script_name, path, usability):
        msg = 'new ' + 'script ' + f'{script_name} ' + f'{path} ' + f'{usability}'
        self.Send_msg(msg)
        os.system(f"touch /home/mehrdad/Documents/my-git/automation/client_cache/{script_name}")

    def Edit_script(self, script_name):
        msg = 'edit ' + 'script ' + f'{script_name}'
        self.Send_msg(msg)
        while True:  # I try to get script content from server
            report = self.Recv_B_msg()
            if report != False:
                break
            else:
                pass
        os.system(f"touch /home/mehrdad/Documents/my-git/automation/client_cache/{script_name}")
        return report

    def Delete_script(self, script_name):
        msg = 'del ' + 'script ' + f'{script_name}'
        self.Send_msg(msg)
        while True:  # I try to get script content from server
            report = self.Recv_msg()
            if report == 'not found':
                return False
            elif report == 'found':
                return True

    def Update_script(self, script_name, new_content):
        ########### First save script on client. ###########
        modify_script = open(f"/home/mehrdad/Documents/my-git/automation/client_cache/{script_name}", mode='w+')
        modify_script.write(new_content)
        modify_script.close()
        ########### Second Send Script to server. ###########
        msg = 'edit ' + 'script ' + 'update ' + f'{script_name}'
        self.Send_msg(msg)
        script = open(f"/home/mehrdad/Documents/my-git/automation/client_cache/{script_name}", mode='r')
        self.Send_B_msg(script.read())
        script.close()

    def Launch_script(self, script_name):
        msg = 'launch ' + f'{script_name}'
        self.Send_msg(msg)

    def Load_all_script(self):
        msg = 'show ' + 'all-script'
        self.Send_msg(msg)
        while True:  # I try to get script data from server
            report = self.Recv_B_msg()
            if report != False:
                break
            else:
                pass
        return report

    def Load_path_script(self, script_name):
        msg = 'show ' + 'script-path ' + f'{script_name}'
        self.Send_msg(msg)
        while True:  # I try to get script data from server
            report = self.Recv_msg()
            if report != False:
                break
            else:
                pass
        return report

    ########################################## Log management section ############# status: implemented ######################
    def Get_Login_log(self, attrib, value):
        msg = 'show ' + 'login-log ' + f'{attrib} ' + f'{value}'
        self.Send_msg(msg)
        while True:  # I try to get logs from server
            report = self.Recv_B_msg()
            if report != False:
                break
            else:
                pass
        return report

    def Get_Action_log(self, attrib, value):
        msg = 'show ' + 'action-log ' + f'{attrib} ' + f'{value}'
        self.Send_msg(msg)
        while True:  # I try to get logs from server
            report = self.Recv_B_msg()
            if report != False:
                break
            else:
                pass
        return report

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
    # print(A.User_find('JAX', '12345'))

    # print(A.Server_add('automation', '123456', 'automation.com', '127.0.0.1', 4444))
    # print(A.Server_update('automation', '123', 'password', '123456'))
    # print(A.Server_del('automation', '123456'))
    # print(A.Server_find('automation', '123456'))
    # print(A.Start_server('automation', '123456', '127.0.0.1', 4444))

    # print(A.Create_script('set-ntp.py', "/home/mehrdad/Documents/my-git/automation/automation_scripts/", "Set ntp protocol"))
    # print(A.Del_script('get-interface.py'))
    # print(A.Up_script('get-interface.py', 'path', "/home/mehrdad/Documents/my-git/automation/automation_scripts/"))
    # print(A.Find_script('put-interface.py'))
    # print(A.Load_script())

    # print(A.Admin_workspace_add('mixtape'))
    # print(A.User_workspace_add('Jax'))
    # print(A.Admin_workspace_update('mixtape', '12345', 'owner', 'Mixtape'))
    # print(A.User_workspace_update('Jax', '1234', 'owner', 'JAX'))
    # print(A.Admin_workspace_del('mixtape', '12345'))
    # print(A.User_workspace_del('Jax', '1234'))
    # print(A.Admin_workspace_find('MixTape'))
    # print(A.User_workspace_find('JAX'))