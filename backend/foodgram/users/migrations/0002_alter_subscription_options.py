# Generated by Django 3.2 on 2023-05-26 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('author',), 'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
    ]
