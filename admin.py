import manage_db
import client

class Admin():
    def __init__(self):
        self.C = client.Client()
        self.db = manage_db.Automation_BD()

    def Login(self, server_ip, server_port, username, password, key):
        C = client.Client()
        return C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

    def Admin_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone):
        report = self.db.Insert_admin(username, self.C.Hash(password), first_name, last_name, birth_year, birth_month, birth_day, email, phone)
        return report

    def Admin_update(self, username, password, attrib, new_value):
        if attrib == 'password':
            hash_pass = self.C.Hash(new_value)
            report = self.db.Update_admin(username, self.C.Hash(password), attrib, hash_pass)
        else:
            report = self.db.Update_admin(username, self.C.Hash(password), attrib, new_value)
        return report

    def Admin_del(self, username, password):
        report = self.db.Delete_admin(username, self.C.Hash(password))
        return report

    def Admin_find(self, username, password):
        report = self.db.Get_attrib_admin(username, self.C.Hash(password))
        if report == False:
            return f'Admin not found with this username: {username}'
        else:
            return report

    def User_add(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission):
        pass
    def User_update(self, username, password, attrib, new_value):
        pass
    def User_del(self, username, password):
        pass
    def User_find(self, username, password):
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

# if __name__ == "__main__":
#     A = Admin()
    # print(A.Admin_add('alex2', '1234', 'alex', 'D', '1990', '6', '5', 'alex@gmail.com', '0933'))
    # print(A.Admin_update('mixtape', '123', 'password', '12345'))
    # print(A.Admin_del('alex2', '1234'))
    # print(A.Admin_find('alex2', '1234'))