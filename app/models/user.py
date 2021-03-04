import app.generator as generator

class User:
    def __init__(self, **kwargs):

        # NOTE: Can either take sqlite (tuple), json (dict) or specified args
        if 'sqlite' in kwargs:
            sqlite = kwargs['sqlite']
            self.id = sqlite[0]
            self.key = sqlite[1]
            self.name = sqlite[2]
            self.email = sqlite[3]
        else:
            self.id = kwargs['id']
            self.key = kwargs['key']
            self.name = kwargs['name']
            self.email = kwargs['email']
    
    # List of all variables for easy access. Used by sqlite3 prepared statements.
    def var_list(self, order):
        # id first
        if order == 'insert':
            return [self.id, self.key, self.name, self.email]
        # id last
        elif order == 'update':
            return [self.key, self.name, self.email, self.id]

    @staticmethod
    def fromJson(json, db):
        return User(
            # Assuming request data => Not accepting manual id/key
            id=generator.gen_id('user', db),
            key=generator.gen_key(db),
            name=json['name'],
            email=json['email'])


    def toJson(self):
        return {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "email": self.email
        }
    