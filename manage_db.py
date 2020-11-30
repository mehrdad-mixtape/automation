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
        pass
    def Delete_user(self, username, password):
        pass
    def Update_user(self, username, password, attrib, new_value):
        pass
    def Get_attrib_user(self, username, password):
        pass

    def Close_connection(self):
        self.connection.close()