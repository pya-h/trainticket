# Generated by Django 4.1.3 on 2023-01-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_rename_date_train_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='time',
            field=models.DateTimeField(),
        ),
    ]