import manage_db

class Normal_user():
    def __init__(self, username, password, fname, lname, email, phone, permission):
        self.username = username
        self.passwoed = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.permission = permission

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