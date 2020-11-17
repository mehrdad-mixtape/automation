import pymongo

class Automation_BD:
    def __init__(self):
        self.connection = pymongo.MongoClient('127.0.0.1', 27017)
        self.automation_db = self.connection['automation_db']
        self.admin_coll = self.automation_db['admins']
        self.user_coll = self.automation_db['users']
        self.server_coll = self.automation_db['server']
        self.workspace_coll = self.automation_db['workspace']
        self.log_coll = self.automation_db['logs']
        self.script_coll = self.automation_db['script']

    def Insert_admin(self, name):
        data = {'name' : name}
        self.admin_coll.insert(data)