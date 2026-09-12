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

Клонуйте репозиторій та перейдіть до його каталогу:

```powershell
git clone <URL_ВАШОГО_РЕПОЗИТОРІЮ>
cd goit-pythonweb-hw-08
```

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
```

## API endpoints

| Метод | Endpoint | Опис |
|---|---|---|
| GET | `/` | Перевірка роботи API |
| GET | `/contacts` | Отримання списку контактів |
| GET | `/contacts/{contact_id}` | Отримання контакту за ID |
| POST | `/contacts` | Створення контакту |
| PATCH | `/contacts/{contact_id}` | Часткове оновлення контакту |
| DELETE | `/contacts/{contact_id}` | Видалення контакту |

## Пошук контактів

Для пошуку використовуйте параметр `search`:

```text
GET /contacts?search=Євген
```

Пошук виконується за іменем, прізвищем, email та назвою компанії.

## Оновлення контакту

Запит до `PATCH /contacts/{contact_id}`:

```json
{
  "phone": "+380501112233",
  "company": "Updated Company"
}
```

Можна передавати лише ті поля, які потрібно змінити.

## Коди відповідей

- `200 OK` — успішне отримання або оновлення;
- `201 Created` — контакт успішно створено;
- `204 No Content` — контакт успішно видалено;
- `404 Not Found` — контакт не знайдено;
- `409 Conflict` — email уже використовується;
- `422 Unprocessable Entity` — помилка валідації даних.

## База даних

Локальний файл бази даних `contacts.db` не додається до Git завдяки `.gitignore`.

