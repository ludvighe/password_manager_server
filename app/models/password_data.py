import app.generator as generator

class PasswordData:
    def __init__(self, **kwargs):

        # NOTE: Can either take sqlite (tuple), json (dict) or specified args
        if 'sqlite' in kwargs:
            sqlite = kwargs['sqlite']
            self.id = sqlite[0]
            self.usr_id = sqlite[1]
            self.title = sqlite[2]
            self.salt = sqlite[3]
            self.count = sqlite[4]
            self.length = sqlite[5]
            self.created = sqlite[6]
            self.last_used = sqlite[7]
        else:
            self.id = kwargs['id']
            self.usr_id = kwargs['usr_id']
            self.title = kwargs['title']
            self.salt = kwargs['salt']
            self.count = kwargs['count']
            self.length = kwargs['length']
            self.created = kwargs['created']
            self.last_used = kwargs['last_used']
    
    # List of all variables for easy access. Used by sqlite3 prepared statements.
    def var_list(self, order):
        # id first
        if order == 'insert':
            return [self.id, self.usr_id, self.title, self.salt, self.count, self.length, self.created, self.last_used]
        # id last
        elif order == 'update':
            return [self.usr_id,self.title, self.salt, self.count, self.length, self.created, self.last_used, self.id]
    
    @staticmethod
    def fromJson(json, usr_id, db=None):
        if db == None:
            id = json['id']
        else:
            id = generator.gen_id('password_data', db)
        print(id)
        return PasswordData(
            # Assuming request data => Not accepting manual id/key
            id=id,
            usr_id=usr_id,
            title=json['title'],
            salt=json['salt'],
            count=json['count'],
            length=json['length'],
            created=json['created'],
            last_used=json['last_used'])

    def toJson(self):
        return {
            "id": self.id,
            "usr_id": self.usr_id,
            "title": self.title,
            "salt": self.salt,
            "count": self.count,
            "length": self.length,
            "created": self.created,
            "last_used": self.last_used
        }