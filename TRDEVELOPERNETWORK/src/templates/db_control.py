from pymongo import MongoClient
class User:
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password
    def control(self):
        user_data={user_name:self.user_name,password:self.password}
        
