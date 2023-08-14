from database.models import Question
from database import db


# Функция добавления вопроса - 7 параметров
def add_question(main_text, v1, v2, v3, v4, correct_answer, level):
    new_question = Question(main_text=main_text,
                            variant_1=v1,
                            variant_2=v2,
                            variant_3=v3,
                            variant_4=v4,
                            correct_answer=correct_answer,
                            level=level)

    db.session.add(new_question)
    db.session.commit()

    return True


# Вывести 20 вопросов (1 параметр - level)
def get_questions_db(level):
    questions = Question.query.filter_by(level=level).all()

    return questions[:21]


# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    question = Question.query.filter_by(question_id=question_id).first()

    return question.correct_answer == user_answer
