from flask import Flask
from database import db


app = Flask(__name__)

# Создаем конфигурацию базы данных дял проекта и указываем путь
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"

# Регистрируем базу на проект
db.init_app(app)
