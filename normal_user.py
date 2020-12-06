import manage_db
import client

class Normal_user():
    def __init__(self):
        self.C = client.Client()
        self.db = manage_db.Automation_BD()
    def Login(self, server_ip, server_port, username, password, key):
        return self.C.Connect_and_authenticate_to_server(server_ip, server_port, username, password, key)

        ########################################## Script management section ############# status: implement 70% ######################

    ########################################## User management section ############# status: implement 70% ######################
    def Show_profile(self, username, password):
        report = self.db.Get_attrib_user(username, password) # report[9] = permission
        if report != False:
            return report # return information of user
        else:
            return report # return False

    ########################################## Script management section ############# status: implement 70% ######################
    def Run_script(self, script_name):
        pass

    def Edit_script(self, script_name, path, permission):
        pass

    def Create_script(self, script_name, path, usability,permission):
        if permission == True:
            report = self.db.Insert_script(script_name, path, usability)
            return report
        else:
            return "Access denied! You have no any permission to create new script"

    def Del_script(self, script_name, permission):
        if permission == True:
            report = self.db.Delete_script(script_name)
            return report
        else:
            return "Access denied! You have no any permission to delete script"

    def Up_script(self, script_name, attrib, new_value, permission):
        if permission == True:
            report = self.db.Update_script(script_name, attrib, new_value)
            return report
        else:
            return "Access denied! You have no any permission to create update script"

    def Find_script(self, script_name, permission):
        if permission == True:
            report = self.db.Get_attrib_script(script_name)
            return report
        else:
            return "Access denied! You have no any permission"

    ########################################## Log management section ############# status: implemented ######################
    def All_login_log(self, permission):
        if permission == True:
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
        else:
            return "Access denied! You have no any permission to see login logs"

    def Login_log(self, attrib, value, permission):
        if permission == True:
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
        else:
            return f"Access denied! You have no any permission to see log: {attrib}:{value}"

    def All_action_log(self, permission):
        if permission == True:
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
        else:
            return "Access denied! You have no any permission to see action logs"

    def Action_log(self, attrib, value, permission):
        if permission == True:
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
        else:
            return f"Access denied! You have no any permission to see log: {attrib}:{value}"

    ########################################## Monitor management section ############# status: none ######################
    def Monitor_server(self):
        pass

    ########################################## SSH management section ############# status: none ######################
    def SSH(self, username, ip_address, permission):
        pass