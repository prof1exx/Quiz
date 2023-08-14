from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Импорт всех функций из файлов для бд
from database.leaderservice import *
from database.questionservice import *
from database.registerservice import *
