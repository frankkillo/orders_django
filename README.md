# orders_django
Тестовая работа, для работы с таблицами Google Sheets. Для запуска приложения есть два способа:
1. Docker
2. Ручной запуск

# 1. Docker
Перейдите в корневую папку и выполните команды:
1.1 Запуск контейнеров используя docker-compose:
```bash
$ docker-compose up -d --build
```
2.2 Необходимо выполнить миграцию в БД:
```bash
$ docker-compose exec web python manage.py migrate --noinput
```
2.3 Проверьте результат:
```bash
$ docker-compose logs -f
```
В случае ошибки:
Если ошибка связана с celery_beat_1 или celery_1, то остановите контейнер и запустите заново:
```bash
$ docker-compose stop
```
```bash
$ docker-compose up -d
```
Если ошибка:
```bash
django.db.utils.OperationalError: FATAL:  database "test_sheets" does not exist
```
выполните команду:
```bash
$ docker-compose down -v
```
и перезапустите команду 1.1.
# 2. Ручной запуск
