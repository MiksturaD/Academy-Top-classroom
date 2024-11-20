from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=100, verbose_name="Email")
    message = models.CharField(max_length=100, verbose_name="Message")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted at")

    def __str__(self):
        return f"{self.name} {self.email} {self.message}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

