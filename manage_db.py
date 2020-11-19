from pymongo import MongoClient
from bson import ObjectId

class Automation_BD:
    def __init__(self):
        self.connection = MongoClient('127.0.0.1', 27017)
        self.automation_db = self.connection['automation_db']
        self.admin_coll = self.automation_db['admin']
        self.user_coll = self.automation_db['user']
        self.server_coll = self.automation_db['server']
        self.workspace_coll = self.automation_db['workspace']
        self.login_log_coll = self.automation_db['login_log']
        self.action_log_coll = self.automation_db['action_log']
        self.script_coll = self.automation_db['script']

    def Insert_admin(self, username, password, fname, lname, email, phone):
        data = { '_id' : username, 'password' : password, 'fname' : fname, 'lname' : lname, 'email' : email, 'phone' : phone, 'permission' : True}
        if self.admin_coll.insert_one(data).acknowledged == True:
            return 'New admin created successfully'
        else:
            return 'Operation failed, please try again'

    def Delete_admin(self, username):
        if self.admin_coll.delete_one({'_id': username}).acknowledged == True:
            return 'Admin deleted successfully'
        else:
            return 'Operation failed, please try again'

    def Update_admin(self, username, attrib, new_value):
        data = {attrib : new_value}
        if self.admin_coll.update_one({'_id': username}, {"$set": data}).acknowledged == True:
            return 'Selected index Update'

    def Get_attrib_admin(self, username):
        if self.admin_coll.find_one({'_id' : username}):
            data = self.admin_coll.find_one({'_id' : username})
            result = []
            for key in data:
                result.append(data[key])
            return result
        else:
            return False

    def Close_connection(self):
        self.connection.close()