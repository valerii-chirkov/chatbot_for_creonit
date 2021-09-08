# chatbot_for_creonit

<h2 align="center"> 
   ⇝ Краткое описание файлов ⇜
</h2>

<h4>100.jpeg - временный файл, в зависимости от имени, будет разная фотография благодаря api</h4>
<h4>_token.py - секретная информация, которая берется из вк</h4>
<h4>bot.py - основной код бота</h4>
<h4>generate_ticket.py - отвечает за рисовку билета/пропуска</h4>
<h4>handlers.py - обычная проверка валидности</h4>
<h4>settings.py - сценарии общения</h4>
<h4>ticket_template.png - шаблон билета, можно нарисовать свой и отредактировать данные в generate_ticket.py</h4>

<h2 align="center"> 
   ⇝ Подготовка ⇜
</h2>

<h3 align="center"> 
Переходим в папку с ботом: 
</h3>

```console
cd chatbot
```

<h3 align="center"> 
Настраиваем окружение и заходим в него:
</h3>

```console
python3 -m venv venv_name
python3 venv/bin/activate
```

<h3 align="center"> 
Обновляем pip:
</h3>

```console
python3 -m pip install --upgrade pip
```

<h3 align="center"> 
Устанавливаем необходимые пакеты:
</h3>

```console
pip3 install -r requirements.txt
```

<h2 align="center"> 
    ⇝ Запускаем бота ⇜
</h2>

```console
python3 bot.py
```

<h2 align="center"> 
    ⇝ Пример билета ⇜
</h2>
<a href="https://ibb.co/J2WY10J"><img src="https://i.ibb.co/VD0F1r4/ticket-example.png" alt="ticket-example" border="0"></a>

<h2 align="center"> 
    ⇝ Возможный сценарий общения ⇜
</h2>

<h4 align="center"> 
    Пользователь: "выаываываыва"
</h4>
<h4 align="center"> 
    Бот: "Не знаю как ответить.Могу сказать когда и где пройдет конференция, а также зарегистрировать на нее. Просто спросите." (Произошла обработка исключений)
</h4>
<h4 align="center"> 
    Пользователь: "Зарегистрируй, пожалуйста"
</h4>
<h4 align="center"> 
    Бот: "Чтобы зарегистрироваться, введите ваше имя. Оно будет написано на бейдже."
</h4>
<h4 align="center"> 
    Пользователь: "Valerii"
</h4>
<h4 align="center"> 
    Бот: "Введите e-mail, мы отправим всю информацию на него."
</h4>
<h4 align="center"> 
    Пользователь: "email@email.ru"
</h4>
<h4 align="center"> 
    Бот: "Спасибо за регистрацию, валера! Мы отправили на email@email.com билет, распечатайте его"
</h4>
<a href="https://ibb.co/J2WY10J"><img src="https://i.ibb.co/VD0F1r4/ticket-example.png" alt="ticket-example" border="0"></a>
