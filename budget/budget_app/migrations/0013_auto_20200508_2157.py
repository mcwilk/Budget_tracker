# Generated by Django 2.2.12 on 2020-05-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0012_expense_dated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-dated_on',)},
        ),
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
    ]
