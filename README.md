## Разворачивание проекта.
 <p>Когда проект будет загружен требуется перейти в корневую папку проекта и выполнить следующие команды: </p>


* Перейти в папку с приложением
```
cd backend
```
* Устанавливаем виртуальное окружение
```
sudo apt install python3-venv
```
* Активируем виртуальное окружение
```
python3 -m venv env
source env/bin/activate
```
* Устанавливаем библиотеки, которые требуются для запуска проекта
```
pip install -r requeriments.txt
```

* Для настройки базы данных у вас уже должен будет запущен сервер postgreSQL. Для правильной настройки просто в backend/settings.py измените данные базы данных.

* Делаем миграцию базы данных
```
python manage.py makemigrations
python manage.py migrate
```
* Создаем суперпользователя
```
python manage.py createsuperuser
```

* После чего запускаем приложение

 <p>Для разворачивания бота вам надо так же:</p>

* Перейти в папку с приложением
```
cd bot
```
* Устанавливаем виртуальное окружение
```
sudo apt install python3-venv
```
* Активируем виртуальное окружение
```
python3 -m venv env
source env/bin/activate
```
* Устанавливаем библиотеки, которые требуются для запуска проекта
```
pip install -r requeriments.txt
```
* Так же требуется указать ключ бота для этого создайте переменную окружения под названием API_KEY и занесите в нее ключ

* После чего запускаем файл main.py


## Создание ответов от бота.

<p> Для того что бы бот отвечал вам надо создать ответы для бота для этого вам надо: </p>

* Зайти по ссылке /admin/
* Войти в раздел ```Настройки сообщений отправляемые ботом```
* Создать для каждого из вариантов поля со своими значениями ответа, после чего бот будет отвечать по данным заполнеными из БД

## Просмотр введенных данных от пользователя.

* Зайти по ссылке /admin/
* Войти в раздел ```Ответы на вопросы```
