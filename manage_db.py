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
        self.log_coll = self.automation_db['log']
        self.script_coll = self.automation_db['script']

    def Insert_admin(self, sname, fname):
        data = {'sname' : sname, 'fname' : fname}
        return self.admin_coll.insert_one(data).acknowledged

    def Delete_admin(self, id):
        return self.admin_coll.delete_one({'_id' : ObjectId(id)})

    def Update_admin(self, id, attrib, new_value):
        data = {attrib : new_value}
        return self.admin_coll.update_one({'_id' : ObjectId(id)}, {"$set": data}).acknowledged

    def Get_attrib_admin(self, id):
        return self.admin_coll.find_one({'_id' : ObjectId(id)})

    def Close_connection(self):
        self.connection.close()


