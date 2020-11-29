import manage_db
import client

class Admin():

    def Login(self, server_ip, server_port, username, password, key):
        C = client.Client()
        return C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

    def Admin_add(self, username, password, administration_password ,fname, lname, email, phone):
        self.username = username
        self.password = password + administration_password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.permission = True

    def Admin_update(self, username, password, fname, lname, email, phone):
        pass
    def Admin_del(self, username, password):
        pass
    def Admin_find(self, username, password):
        pass

    def User_add(self, username, password, fname, lname, email, phone, permission):
        pass
    def User_update(self, username, password, fname, lname, email, phone, permission):
        pass
    def User_del(self, username):
        pass
    def User_find(self, username):
        pass

    def Run_script(self, script_name):
        pass
    def Create_script(self, script_name, path):
        pass
    def Edit_script(self, script_name, path):
        pass
    def Del_script(self, script_name, path):
        pass

    def Show_login_log(self):
        pass
    def Show_action_log(self):
        pass

    def Monitor_server(self):
        pass

    def SSH(self, username, ip_address):
        pass