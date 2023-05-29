import csv

from django.conf import settings
from django.core.management import BaseCommand

from api_yamdb.reviews.models import (
    User, Category, Genre, Title, Review, Comment, GenreTitle
)


TABLES = (
    (User, 'static/data/users.csv'),
    (Category, 'static/data/category.csv'),
    (Genre, 'static/data/genre.csv'),
    (GenreTitle, 'static/data/genre_title.csv'),
    (Title, 'static/data/titles.csv'),
    (Review, 'static/data/review.csv'),
    (Comment, 'static/data/comments.csv')
)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            for model, base in TABLES:
                with open(
                    f'{settings.BASE_DIR}/static/data/{base}',
                    encoding='utf8'
                ) as csv_file:
                    reader = csv.DictReader(csv_file)
                    for row_dict in reader:
                        model_date = model(data=row_dict)
                        if model_date.is_valid():
                            model_date.save()
                    self.stdout.write(self.style.SUCCESS(
                        f'Данные из файла {base} успешно загружены'
                    ))
            self.stdout.write(self.style.SUCCESS('Все файлы загружены'))
        except Exception as eroor:
            raise Exception(f'Ошибка {eroor}')
