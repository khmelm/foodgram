# Финальный проект курса - "Python-Разработчик" - Foodgram - продуктовый помощник
<<<<<<< HEAD
![example workflow](https://github.com/khmelm/foodgram-project-react/actions/workflows/main.yml/badge.svg)  
=======
![example workflow](https://github.com/khmelm/Foodgram/actions/workflows/main.yml/badge.svg)  
>>>>>>> 40d70ec25adc3db18fb9c2ccbf8d01b81357bca0

## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

## Описание проекта
Foodgram - это онлайн-сервис, который предоставляет возможность пользователям публиковать свои рецепты, подписываться на рецепты других пользователей, добавлять понравившиеся рецепты в список "Избранное" и скачивать списки продуктов в формате .txt для покупок.

Архитектура проекта включает несколько Docker контейнеров: backend-приложение API, PostgreSQL-базу данных, nginx-сервер и frontend-контейнер.

Для обеспечения надежности и автоматизации развертывания проекта реализованы CI (непрерывная интеграция) и CD (непрерывная доставка). При каждом пуше изменений в главную ветку проект проходит автоматичесное тестирование на соответствие требованиям PEP8 (стандарт оформления кода на языке Python). После успешного прохождения тестов, собранный Docker-образ backend-контейнера автоматически размещается на платформе DockerHub. Затем развертывание проекта автоматически выполняется на боевом сервере, где запускаются контейнеры с backend-приложением, веб-сервером nginx и базой данных PostgreSQL.

[Ссылка на проект на сервере Yandex.Cloud](http://158.160.60.63/)

## Системные требования
- Python 3.9
- Docker
- Works on Linux, Windows, macOS

## Запуск проекта в контейнере
Клонируйте репозиторий и перейдите в него в командной строке.
Создайте и активируйте виртуальное окружение:
```
git clone https://github.com/khmelm/foodgram-project-react.git
cd backend
cd foodgram
```
Backend запускается на порту 8000. PostgreSQL поднимается на 5432 порту, оба порта должны быть свободны.
Cоздать и открыть файл .env с переменными окружения:
```
cd infra
touch .env
```
Заполнить .env файл с переменными окружения по примеру INFRA/example.env. 

```
Установить и запустить приложения в контейнерах (образ для контейнера backend загружается из DockerHub):
```
docker-compose up -d
```
Запустить миграции, создать суперюзера, собрать статику и заполнить таблицы БД с ингредиентами и тегами:
```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input 

docker-compose exec backend python manage.py ingredients_import

docker-compose exec backend python manage.py tags_import
```
