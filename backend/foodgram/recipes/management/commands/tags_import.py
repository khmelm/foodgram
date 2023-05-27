from csv import reader

from django.core.management.base import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    """Ingredients loader."""
    help = "Load ingredients from csv file (should be in '/backend/data')."

    def handle(self, *args, **kwargs):
        tag_list = []
        with open(
                'data/tags.csv', 'r', encoding='UTF-8', newline='') as file:
            csv_reader = reader(file)

            for row in csv_reader:
                name = row[0]
                color = row[1]
                slug = row[2]
                tag = Tag(
                    name=name,
                    color=color,
                    slug=slug
                )
                tag_list.append(tag)
        Tag.objects.bulk_create(tag_list)

        self.stdout.write(self.style.SUCCESS('Тэги загружены!'))
