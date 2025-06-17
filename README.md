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
cd backend
```
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

###Скришоты 
![image](https://github.com/user-attachments/assets/55a23b61-670b-4e9d-8029-2c8368fd8109)
![image](https://github.com/user-attachments/assets/8b7af6fd-ac64-4eed-85dc-ac09873c8675)
![image](https://github.com/user-attachments/assets/f302d638-df57-45e2-a48e-909df217eee3)
![image](https://github.com/user-attachments/assets/161728cd-5f5c-4444-bb28-9bcc98669188)
Управление справочниками доступно в админ-панели
![image](https://github.com/user-attachments/assets/a346df51-98e1-4ab5-b5de-03e0811fed67)


Админ панель доступна по адресу: http://127.0.0.1:8000/admin/

Автор: Охотина Ксения Николаевна - [github.com/okhotinaks](https://github.com/okhotinaks)
