# Generated by Django 3.2.6 on 2021-09-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myToDo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
