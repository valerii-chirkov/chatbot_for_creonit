"""
Bot's behaviour
"""

INTENTS = [
    {
        'name': 'Дата проведения',
        'tokens': ('когда', 'сколько', 'дата', 'дату', '1',),
        'scenario': None,
        'answer': 'Конференция проводится 15 апреля, регистрация начнется в 10 утра.'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро', '2', ),
        'scenario': None,
        'answer': 'Конференция пройдет в павильоне 18Г в Экспоцентре.'
    },
    {
        'name': 'Регистрация',
        'tokens': ('регист', 'добав', '3', ),
        'scenario': 'registration',
        'answer': None
    },
    {
        'name': 'Благодарность',
        'tokens': ('спс', 'спасибо', '4', ),
        'scenario': None,
        'answer': 'Пожалуйста!'
    },

]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы зарегистрироваться, ввдеите ваше имя. Оно будет написано на бейдже.',
                'failure_text': 'Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз',
                'handler': 'handle_name',
                'next_step': 'step2',
            },
            'step2': {
                'text': 'Введите e-mail, мы отправим всю информацию на него.',
                'failure_text': 'В адресе ошибка. Попробуйте еще раз',
                'handler': 'handle_email',
                'next_step': 'step3',
            },
            'step3': {
                'text': 'Спасибо за регистрацию, {name}! Ваш билет ниже, копию отправили на {email}, распечатайте его',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None,
            },
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как ответить.' \
                 'Могу сказать когда и где пройдет конференция, а также зарегистрировать на нее. Просто спросите.'


DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='',
    host='localhost',
    database='chatbot'
)