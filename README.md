# yamdb_final
![example branch parameter](https://github.com/SoliDeoGloriaaa/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). На реализацию проекта потребовалось 15 дней!


## Технологии и их версии
В проекте использовались такие технологии, как:
- asgiref==3.2.10
- Django==2.2.16
- django-filter==2.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.8.0
- gunicorn==20.0.4
- psycopg2-binary==2.8.6
- PyJWT==2.1.0
- pytz==2020.1
- sqlparse==0.3.1
- pytest
- pytest-django
- pytest-pythonpath

## Авторы
Над проектом работал студент Backend факультета Яндекс.Практикум:
+ [Александр](https://github.com/SoliDeoGloriaaa)


## Как запустить проект пользователям системы Windows
1. Проверьте, установлен ли у вас Docker на компьютере
```
docker -v
```

2. Клонировать репозиторий командой
```
git clone git@github.com:SoliDeoGloriaaa/yamdb_final.git
```

3. Запустить ```docker-compose```
    Выполнить команду
    ```
    docker-compose up -d
    ```

4. Выполнить миграции
```
docker-compose exec web python manage.py migrate
```

5. Прогрузить статику
```
docker-compose exec web python manage.py collectstatic
```

## Шаблон наполнения .env файла расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres                        # имя базы данных
POSTGRES_USER=postgres                  # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres              # пароль для подключения к БД (установите свой)
DB_HOST=db                              # название сервиса (контейнера)
DB_PORT=5432                            # порт для подключения к БД 
```

## Примеры запросов к API

Документацию к API можно посмотреть на запущенном сервере через путь `/redoc/`