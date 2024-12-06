# Generated by Django 4.2.16 on 2024-11-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('message', models.CharField(max_length=100, verbose_name='Сообщение')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted at')),
            ],
        ),
    ]