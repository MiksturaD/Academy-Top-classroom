from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.CharField(max_length=100, verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость позиции")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано : ")

    def __str__(self):
        return f"{self.name} {self.description} {self.price}"
