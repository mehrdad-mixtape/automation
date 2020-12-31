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
        while True:  # I try to get True from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

    def Admin_update(self, username, password, attrib, new_value):
        if attrib == 'password':
            msg = 'edit ' + 'admin ' + f"{username} {self.C.Hash(password)} {attrib} {self.C.Hash(new_value)}"

        else:
            msg = 'edit ' + 'admin ' + f"{username} {self.C.Hash(password)} {attrib} {new_value}"

        self.Send_msg(msg)
        while True:  # I try to get True from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

    ########################################## User management section ############# status: implemented ######################
    def User_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission):
        msg = 'new ' + 'user ' + f"{username} {self.C.Hash(password)} {first_name} {last_name} {birth_year} {birth_month} {birth_day} {email} {phone} {permission}"
        self.Send_msg(msg)

    def User_del(self, username, password):
        msg = 'del ' + 'user ' + f"{username} {self.C.Hash(password)}"
        self.Send_msg(msg)
        while True:  # I try to get True from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

    def User_update(self, username, password, attrib, new_value):
        if attrib == 'password':
            msg = 'edit ' + 'user ' + f"{username} {self.C.Hash(password)} {attrib} {self.C.Hash(new_value)}"

        else:
            msg = 'edit ' + 'user ' + f"{username} {self.C.Hash(password)} {attrib} {new_value}"

        self.Send_msg(msg)
        while True:  # I try to get True from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

    ########################################## Server management section ############# status: implemented ######################
    def Server_add(self, hostname, password, domain, ip, port):
        msg = 'new ' + 'server ' + f"{hostname} {self.C.Hash(password)} {domain} {ip} {port}"
        self.Send_msg(msg)

    def Server_del(self, hostname, password):
        msg = 'del ' + 'server ' + f"{hostname} {self.C.Hash(password)}"
        self.Send_msg(msg)
        while True:  # I try to get True from server
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
            msg = 'edit ' + 'server ' + f"{hostname} {self.C.Hash(password)} {attrib} {self.C.Hash(new_value)}"

        else:
            msg = 'edit ' + 'server ' + f"{hostname} {self.C.Hash(password)} {attrib} {new_value}"

        self.Send_msg(msg)
        while True:  # I try to get True from server
            report = self.Recv_msg()
            if report != False:
                if report == 'False':
                    return False
                else:
                    return True
            else:
                pass

    def Start_server(self, hostname, password, ip, port):
        report = self.db.Get_attrib_server(hostname, self.C.Hash(password)) # authenticate server
        if report == False: # if authentication operation was failed, server return False and run_server_form.py can handle it.
            # self.db.Record_action_log(f'{hostname}:server {ip}:{port} had problem for running', hostname)
            return report
        else:
            # self.db.Record_action_log(f'{hostname}:server was running with {ip}:{port}', hostname)
            S = server.Server(ip, port)
            return S.Run_Server() # if ip/port cannot bind to server, server return "internal error" and run_server_form can handle it.

    ########################################## Script management section ############# status: implemented ######################
    def Create_script(self, script_name, path, usability):
        msg = 'new ' + 'script ' + f"{script_name} {path} {usability}"
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