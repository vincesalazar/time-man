# Generated by Django 3.0.3 on 2020-04-02 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList_app', '0004_auto_20200401_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default='00-00-0000'),
        ),
    ]
