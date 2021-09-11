# Установка
Клонируем репозиторий и переходим в папку с проектом:
```bash
git clone https://github.com/devsia93/django_poll.git

cd django_polls
```

Копируем файл `example.env` в файл `.env`:

```bash
cp example.env .env
```

Устанавливаем виртуальное окружение:

```bash
python3.9 -m venv venv
```

Поднимаем базу данных с помощью докера:

```bash
docker-compose up
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Устанавливаем зависимости, применяем миграции:

```bash
pip install -r requirements.txt

python manage.py migrate
```

Создаем суперпользователя и отвечаем на вопросы, которые задаст утилита:

```bash
python manage.py createsuperuser
```

Запускаем сервер:

```bash
python manage.py runserver
```