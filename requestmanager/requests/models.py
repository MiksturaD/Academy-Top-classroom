from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    email = models.EmailField(max_length=100, verbose_name="Email")
    message = models.CharField(max_length=100, verbose_name="Сообщение")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted at")

    def __str__(self):
        return f"{self.name} {self.email} {self.message}"


