from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Automation_BD:
    def __init__(self):
        self.connection = MongoClient('127.0.0.1', 27017) # I should create a connection to mongo
        self.automation_db = self.connection['automation_db'] # I create my db: automation_db
        ############# create collections that stored on db ############
        self.admin_coll = self.automation_db['admin']
        self.user_coll = self.automation_db['user']
        self.server_coll = self.automation_db['server']
        self.workspace_coll = self.automation_db['workspace']
        self.login_log_coll = self.automation_db['login_log']
        self.action_log_coll = self.automation_db['action_log']
        self.script_coll = self.automation_db['script']

    ################################## Admin Section ##################################
    def Insert_admin(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone):
        data = {
            'username' : username,
            'password' : password,
            'first_name' : first_name,
            'last_name' : last_name,
            'birth_year' : birth_year,
            'birth_month' : birth_month,
            'birth_day' : birth_day,
            'email' : email,
            'phone' : phone,
            'permission' : True,
            'record_date' : datetime.now().strftime("%y-%m-%d %H:%M:%S")
        }
        if self.admin_coll.insert_one(data).acknowledged == True:
            return 'New admin created successfully'
        else:
            return 'Operation failed, please try again'

    def Delete_admin(self, username, password):
        data = {
            'username' : username
        }
        if self.Get_attrib_admin(username, password) != False:
            if self.admin_coll.delete_one(data).acknowledged == True:
                return 'Admin deleted successfully'
            else:
                return 'Operation failed, please try again'
        else:
            return f'Admin not found with this username: {username}'

    def Update_admin(self, username, password, attrib, new_value):
        data = {
            attrib : new_value
        }
        if self.Get_attrib_admin(username, password) != False:
            if self.admin_coll.update_one({'username': username}, {"$set": data}).acknowledged == True:
                return 'Operation complete'
            else:
                return 'Operation failed, please try again'
        else:
            return f'Admin not found with this username: {username}'

    def Get_attrib_admin(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        if self.admin_coll.find_one(data):
            all_attribs = self.admin_coll.find_one(data)
            result = []
            for key in all_attribs:
                result.append(all_attribs[key])
            return result
        else:
            return False

    ################################## User Section ##################################
    def Insert_user(self, username, password, first_name, last_name, birth_year, birth_month, birth_day, email, phone, permission):
        data = {
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'birth_year': birth_year,
            'birth_month': birth_month,
            'birth_day': birth_day,
            'email': email,
            'phone': phone,
            'permission': permission,
            'record_date': datetime.now().strftime("%y-%m-%d %H:%M:%S")
        }
        if self.user_coll.insert_one(data).acknowledged == True:
            return 'New User created successfully'
        else:
            return 'Operation failed, please try again'

    def Delete_user(self, username, password):
        data = {
            'username': username
        }
        if self.Get_attrib_user(username, password) != False:
            if self.user_coll.delete_one(data).acknowledged == True:
                return 'User deleted successfully'
            else:
                return 'Operation failed, please try again'
        else:
            return f'Admin not found with this username: {username}'

    def Update_user(self, username, password, attrib, new_value):
        data = {
            attrib: new_value
        }
        if self.Get_attrib_user(username, password) != False:
            if self.user_coll.update_one({'username': username}, {"$set": data}).acknowledged == True:
                return 'Operation complete'
            else:
                return 'Operation failed, please try again'
        else:
            return f'User not found with this username: {username}'

    def Get_attrib_user(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        if self.user_coll.find_one(data):
            all_attribs = self.user_coll.find_one(data)
            result = []
            for key in all_attribs:
                result.append(all_attribs[key])
            return result
        else:
            return False

    ################################## Login log Section ##################################
    def Record_login_log(self, content, username):
        data = {
            'year': datetime.now().strftime("%y"),
            'mouth': datetime.now().strftime("%m"),
            'day': datetime.now().strftime("%d"),
            'hour': datetime.now().strftime("%H"),
            'minute': datetime.now().strftime("%M"),
            'second': datetime.now().strftime("%S"),
            'content': content,
            'username': username
        }
        if self.login_log_coll.insert_one(data).acknowledged == True:
            return True

    def Show_all_login_log(self):
        return list(self.login_log_coll.find())

    def Show_login_log(self, attrib, value):
        data = {
            attrib: value
        }
        return list(self.login_log_coll.find(data))

    ################################## Login log Section ##################################
    def Record_action_log(self, content, username):
        data = {
            'year': datetime.now().strftime("%y"),
            'mouth': datetime.now().strftime("%m"),
            'day': datetime.now().strftime("%d"),
            'hour': datetime.now().strftime("%H"),
            'minute': datetime.now().strftime("%M"),
            'second': datetime.now().strftime("%S"),
            'content': content,
            'username': username
        }
        if self.action_log_coll.insert_one(data).acknowledged == True:
            return True

    def Show_all_action_log(self):
        return list(self.action_log_coll.find())

    def Show_action_log(self, attrib, value):
        data = {
            attrib: value
        }
        return list(self.action_log_coll.find(data))

    ################################## Close Connection Section ##################################
    def Close_connection(self):
        self.connection.close()