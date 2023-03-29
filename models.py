from peewee import *
from datetime import datetime

# now = datetime.now()  # Работа с временем

db = SqliteDatabase('user.db')  # Указываем с какой базой данных будем работать. Она обязательно должна быть в той папке в которой находится этот файл


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)
    #ref = IntegerField(default=0)
    dedicate = IntegerField(default=0)
    last_msg_sec = IntegerField(default=0)
    last_msg_min = IntegerField(default=0)

    # Получение данных user-а
    @classmethod
    def get_user(cls, user_id):
        return cls.get(Users.user_id == user_id)

    @classmethod
    def get_dedicate(cls, user_id, msg, i):
        if i == 1:
            return cls.get(Users.user_id == user_id).dedicate
        elif i == 2:
            server = cls.get_user(user_id)
            server.dedicate += int(msg)
            server.save()

    # Получение кол-ва рефералов
    # @classmethod
    # def get_ref_count(cls, user_id):
    #     return cls.get(Users.user_id == user_id).ref

    @classmethod
    def get_last_msg_time(cls, user_id, i, sec_or_min):
        if i == 1:
            return cls.get(Users.user_id == user_id).last_msg_sec
        elif i == 2:
            return cls.get(Users.user_id == user_id).last_msg_min
        elif i == 3:
            sec = cls.get_user(user_id)
            sec.last_msg_sec = sec_or_min
            sec.save()
        elif i == 4:
            min = cls.get_user(user_id)
            min.last_msg_min = sec_or_min
            min.save()

    # #
    # @classmethod
    # def increase_join_date(cls, user_id):
    #     users = cls.get_user(user_id)
    #     users.join_date = "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour,
    #                                                now.minute)  # "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    #     users.save()

    #
    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    #
    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)

'''
db = SqliteDatabase('dedicate.db')  # Указываем с какой базой данных будем работать. Она обязательно должна быть в той папке в которой находится этот файл

class BaseModel(Model):
    class Meta:
        database = db

class Dedicate(BaseModel):
    text = TextField(default='1')

    @classmethod
    def create_user(cls, text):
        user, created = cls.get_or_create(text = text)'''