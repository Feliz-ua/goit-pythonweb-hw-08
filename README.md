# Contacts REST API

REST API для зберігання та управління контактами. Проєкт створено з використанням FastAPI та SQLAlchemy.

## Можливості

- створення контакту;
- отримання списку контактів;
- отримання контакту за ідентифікатором;
- пошук контактів;
- часткове оновлення контакту;
- видалення контакту;
- перевірка даних через Pydantic;
- автоматична документація Swagger UI та ReDoc;
- збереження даних у SQLite.

## Структура проєкту

```text
go it-pythonweb-hw-08/
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Технології

- Python 3.11+;
- FastAPI;
- Uvicorn;
- SQLAlchemy;
- Pydantic;
- SQLite.

## Встановлення
Створіть віртуальне середовище:

```powershell
python -m venv .venv
```

Активуйте його у Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Встановіть залежності:

```powershell
pip install -r requirements.txt
```

## Запуск

Запустіть сервер командою:

```powershell
uvicorn app.main:app --reload --port 8001
```

API буде доступний за адресою:

```text
http://127.0.0.1:8001
```

## Документація API

Swagger UI:

```text
http://127.0.0.1:8001/docs
```

ReDoc:

```text
http://127.0.0.1:8001/redoc
