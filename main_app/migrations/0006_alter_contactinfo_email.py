# Generated by Django 5.0.7 on 2024-08-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_contactinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
