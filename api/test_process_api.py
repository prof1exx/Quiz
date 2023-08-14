from api import api_bp
from database import get_questions_db, check_user_answer_db, user_end_test_db


# URL для получения вопросов
@api_bp.route('/get-questions/<int:level>', methods=['GET'])
def get_questions(level: int):
    result = get_questions_db(level)

    return {'status': 1, 'questions': result}


# URL для проверки ответа пользователя
@api_bp.route('/check-answer/<int:question_id>/<int:user_answer>', methods=['POST'])
def check_user_answer(question_id: int, user_answer: int):
    result = check_user_answer_db(question_id, user_answer)

    if result:
        return {'status': 1}

    else:
        return {'status': 0}


# URL для завершения тестов и получения результатов тестов
@api_bp.route('/done/<int:user_id>/<int:correct_answers>/<int:level>', methods=['POST'])
def commit_user_answers(user_id: int, correct_answers: int, level: int):
    result = user_end_test_db(user_id, correct_answers, level)

    return {'status': 1, 'correct_answers': correct_answers, 'position_on_top': result}
