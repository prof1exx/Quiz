from database.models import User
from database import db


# Функции регистрации пользователя
def register_user_db(name, phone_number):
    # Проверка пользователя на наличие в базе
    checker = User.query.filter_by(phone_number=phone_number).first()

    # Если есть пользователь
    if checker:
        return checker.id

    # Добавление данных в базу
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return new_user.id
