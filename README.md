# insurance-calculation

API сервис по расчёту стоимости страхования в зависимости от типа груза и объявленной стоимости

## Технологии

* Python 3.10
* FastApi
* SQLAlchemy
* Kafka

## Разработка

Проект использует ряд утилит для анализа кода 

Пре-коммит хуки:
* black - форматирование
* mypy - статический анализ
* ruff - линтер

Установка
```
apt install pre-commit
pre-commit install
```
Окружение для разработки: docker-compose.local.yml

## Сборка и запуск

```
docker-compose -f docker-compose.prod.yml up --build -d
```
