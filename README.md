# Документация

## Установка и запуск приложения

### Требования

- Python 3.x
- Django (последняя стабильная версия)
- Django REST Framework (DRF)
- PostgreSQL

### Установка

1. **Скачайте или клонируйте репозиторий:**

   ```bash
   git clone https://github.com/omnik2026/test_task/tree/main

2. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python -m venv env
   .\env\Scripts\activate
   cd backend

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   
1. **Настройте базу данных:**

   ```bash
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': '',  # Имя вашей базы данных
         'USER': '',  # Имя пользователя базы данных
         'PASSWORD': '',  # Пароль пользователя базы данных
         'HOST': '',  # Хост базы данных (обычно 'localhost')
         'PORT': '',  # Порт базы данных (по умолчанию 5432)
      }
   }

Для использования SQLite (по умолчанию):

   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
5. **Выполните миграции базы данных:**
   ```bash
   python manage.py migrate

6. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser

**Запуск сервера разработки**
Запустите сервер разработки с помощью следующей команды:

   ```bash
   python manage.py runserver

 ```
Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000/, чтобы увидеть работающее приложение.


## **Использование API**

### Конечные точки API
- GET /api/cars/ — получение списка автомобилей.
- GET /api/cars/<id>/ — получение информации о конкретном автомобиле.
- POST /api/cars/ — создание нового автомобиля.
- PUT /api/cars/<id>/ — обновление информации о автомобиле.
- DELETE /api/cars/<id>/ — удаление автомобиля.
- GET /api/cars/<id>/comments/ — получение комментариев к автомобилю.
- POST /api/cars/<id>/comments/ — добавление нового комментария к автомобилю.


