# Generated by Django 5.0.7 on 2024-08-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeTitle',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'recipe_title',
            },
        ),
    ]
