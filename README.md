# orders_django [ссылку на Google Sheets документ](https://docs.google.com/spreadsheets/d/1vS9jEfk2Zz4LpR7mLKp2RtOmRaw1dWWZn1fpdUozdA0/edit#gid=0)
## Фрон-енд: https://github.com/frankkillo/orders_django.git
### Тестовая работа, для работы с таблицами Google Sheets. Для запуска приложения есть два способа:
1. Docker
2. Ручной запуск

# 1. Docker
Перейдите в корневую папку и выполните команды в консоле:
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
#### Для ручного запуска необходимо убедиться, что на. вашем ПО установлены [PostgreSQL](https://www.postgresql.org/) , [Redis](https://redis.io)
2.1 Создайте БД PostgreSQL и измените параметры в файле **.env.dev**. 
(Мы расчитываем, что вы знаете как правильно заполнить значения переменных)

2.2 Запустите Redis, проверить можно командой:
```bash
$ redis ping
PONG
```
ответ должен быть PONG.
2.3 Для продолжения требуется новая консоль. Мы расчитываем, что вы создали виртуальное окружение и все пакеты из файла **requirements.txt** были установлены.
*В виртуальной среде экспортируйте переменные из файла **.env.dev**!!!*
Выполните миграции в БД:
```bash
$ python manage.py migrate
```
2.4 После выполнения миграций, запустите Django:
```bash
$ python manage.py runserver
```
убедитесь, что запуск прошел успешно.
2.5 Откройте дополнительную консоль и *экспортируйте переменные из файла **.env.dev**.* Запустите команду:
```bash
$ celery -A orders_django beat -l INFO
```
команда запустит процесс выставление задач для прослушки таблицы Google Sheets в очередь, каждые 30 сек.
Убедитесь в отсутсвие ошибок.
2.6 Откройте еще дополнительную консоль и *экспортируйте переменные из файла **.env.dev**.* Запустите команду:
```bash
$ celery -A orders_django worker -l INFO
```
команда запустит процесс выполнения задач из очереди.
Убедитесь в отсутсвие ошибок. **Обязательно** *экспортируйте переменные из файла **.env.dev** и что миграции в БД так же были выполнены.*

#### Программа успешно запущена. Проверить результаты можно по ссылке http://localhost/api/v1/products или через [админ-панель](http://localhost/admin) , прежде создав суперюзера.
