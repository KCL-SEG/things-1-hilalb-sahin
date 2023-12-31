# Generated by Django 4.2.6 on 2023-10-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_alter_thing_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='thing',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
