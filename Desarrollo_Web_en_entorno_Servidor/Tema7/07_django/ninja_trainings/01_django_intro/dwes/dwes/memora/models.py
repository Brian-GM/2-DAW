from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Note(models.Model):
    note = models.TextField()
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete = models.CASCADE)

