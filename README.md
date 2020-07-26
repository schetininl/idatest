# Инструкцию по развороту и запуску проекта

1. Скачать проект или клонировать с помощью git (git clone https://github.com/schetininl/idatest.git)

2. Перейти в каталог с проектом и создать виртуальное окружение (python3 -m venv venv)

3. Запустить виртуальное окружение (source venv/bin/activate) на Mac/Linux или (source venv/Scripts/activate) на Windows

4. Установить все необходимые пакеты, указанные в файле requirements.txt (pip install -r requirements.txt)

5. Запустить миграции (python manage.py migrate)

6. Для проверки работы проекта запустить тестовый сервер (python manage.py runserver)
