# Generated by Django 5.1.2 on 2024-10-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_user_num_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
