# Generated by Django 5.1.2 on 2024-10-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_rename_mail_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=15),
        ),
    ]
