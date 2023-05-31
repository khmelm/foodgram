from csv import reader

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    """Ingredients loader."""
    help = "Load ingredients from csv file (should be in '/backend/data')."

    def handle(self, *args, **kwargs):
        ingredient_list = []
        with open(
            'data/ingredients.csv',
            'r',
            encoding='UTF-8',
            newline=''
        ) as file:
            csv_reader = reader(file)

            for row in csv_reader:
                name = row[0]
                measurement_unit = row[1]
                ingredient = Ingredient(
                    name=name,
                    measurement_unit=measurement_unit
                )
                ingredient_list.append(ingredient)
        Ingredient.objects.bulk_create(ingredient_list)

        self.stdout.write(self.style.SUCCESS('Ингредиенты загружены!'))
