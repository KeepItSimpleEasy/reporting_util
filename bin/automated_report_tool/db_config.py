class DBConfig:
    def __init__(self, db='', username='', password=''):
        self.__db = db
        self.__username = username
        self.__password = password

    def get_db(self):
        db = self.__db
        return db

    def set_db(self, db):
        self.__db = db

    def get_username(self):
        username = self.__username
        return username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        password = self.__password
        return password

    def set_password(self, password):
        self.__password = password
