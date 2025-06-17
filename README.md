# Веб-сервис для управления движением денежных средств (ДДС)

## Описание 
Веб-приложение, которое позволяет пользователям создавать, редактировать, удалять и просматривать записи о движении денежных средств.

### Демо-версия : 
[okhotinaks.pythonanywhere.com](https://okhotinaks.pythonanywhere.com/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:okhotinaks/cash_flow.git
```
```
cd cash_flow
```

Создать и активировать виртуальное окружение:
```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграци:
```
cd backend
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Создать суперюзера:
```
python manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

Админ панель доступна по адресу: http://127.0.0.1:8000/admin/

### Управление справочниками доступно в админ-панели
![image](https://github.com/user-attachments/assets/5542de74-d4b3-4055-a9c5-30d86cac44a3)

Автор: Охотина Ксения Николаевна - [github.com/okhotinaks](https://github.com/okhotinaks)
