# Kittygram

### Статус актуального workflow 
![workflow status](https://github.com/samirumir/kittygram_final/actions/workflows/main.yml/badge.svg)

## Описание
Этот проект, социальная сеть, для обмена фотографиями любимых питомцев. Предназанечна для загрузки, описания и краткой информации о котах, и распространением информацией о них с другими пользователями.

**Инструменты и стек:** #Python #Django #Docker #API #Nginx #Djoser #Gunicorn #JSON #YAML #Postman #Visual Studio Code

## Запуск
Запуск проекта выполняется с удаленного сервера. Рассмотрим процесс выполнения 

1. В корневой директории проекта необходимо создать и заполнить файл **.env** с переменными окружения:
```bash
sudo nano .env
```

2. Добавляем следующие переменные:
```nano
ENABLE_POSTGRES_DB
POSTGRES_DB=admin
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
DB_HOST=db
DB_PORT=5432
SECRET_KEY=...
DEBUG=... # True/False
ALLOWED_HOSTS=127.0.0.1, localhost, **your_domain**
```

3. Установка утилиты Docker Compose:
```bash
sudo apt update
sudo apt-get install docker-compose-plugin 
```

4. В корневую директорию проекта копируем файл `docker-compose.production.yml` и запускаем Docker Compose:
```bash
sudo docker compose -f docker-compose.production.yml up
```

5. Выполняем миграции с запущенным проектом:
```bash
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```
6. Собираем статику и копируем в папку статики, где хранится backend:
```bash
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/
```


## Примеры запросов 

Добавить питомца: POST `/cats/add`

Редактировать питомца: PUTCH `/cats/edit`

Просмотр питомца: GET `/cats/{cat_id}`

##### Автор проекта: Самир Ханкишиев
