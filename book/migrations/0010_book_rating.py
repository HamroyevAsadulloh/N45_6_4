# Generated by Django 5.0.7 on 2024-07-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]