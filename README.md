# Веб-сервис для управления движением денежных средств (ДДС)

## Описание 
Веб-приложение, которое позволяет пользователям создавать, редактировать, удалять и просматривать записи о движении денежных средств.

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
python3 manage.py migrate
```

Создать суперюзера:
```
python manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```