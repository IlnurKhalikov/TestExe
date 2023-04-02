from peewee import *

# now = datetime.now()  # Работа с временем

db = SqliteDatabase('user.db')  # Указываем с какой базой данных будем работать. Она обязательно должна быть в той папке в которой находится этот файл


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)
    balance = IntegerField(default=0)
    n = IntegerField(default=0)

        # Получение данных user-а
    @classmethod
    def get_user(cls, user_id):
        return cls.get(Users.user_id == user_id)
    
    @classmethod
    def get_n(cls, user_id, msg, i):
        if i == 1:
            return cls.get(Users.user_id == user_id).n
        elif i == 2:
            server = cls.get_user(user_id)
            server.n += msg
            server.save()

    @classmethod
    def get_balance(cls, user_id, msg, i):
        if i == 1:
            return cls.get(Users.user_id == user_id).balance
        elif i == 2:
            server = cls.get_user(user_id)
            server.balance += msg
            server.save()

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    #
    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)
