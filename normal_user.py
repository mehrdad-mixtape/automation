import manage_db
import client

class Normal_user():

    def Login(self, server_ip, server_port, username, password, key):
        C = client.Client()
        return C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

    def Run_script(self, script_name):
        pass
    def Create_script(self, script_name, path, permission):
        pass
    def Edit_script(self, script_name, path, permission):
        pass
    def Del_script(self, script_name, path, permission):
        pass

    def Show_login_log(self, permission):
        pass
    def Show_action_log(self, permission):
        pass

    def Monitor_server(self):
        pass

    def SSH(self, username, ip_address, permission):
        pass