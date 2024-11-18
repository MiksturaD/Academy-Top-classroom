from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="title")
    content = models.CharField(max_length=200, verbose_name="content")
    pub_date = models.DateField(verbose_name='date_published')

    def __str__(self):
        return self.title
