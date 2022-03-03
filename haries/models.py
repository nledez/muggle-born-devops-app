from django.db import models


class Diary(models.Model):
    title = models.CharField(max_length=25, unique=True)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
