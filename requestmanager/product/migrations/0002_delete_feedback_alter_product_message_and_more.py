# Generated by Django 5.1.3 on 2024-11-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AlterField(
            model_name='product',
            name='message',
            field=models.CharField(max_length=100, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название товара'),
        ),
    ]