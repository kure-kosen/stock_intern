from django.db import models
from accounts.models import User
import datetime


class Category(models.Model):
    now = datetime.datetime.now
    category_name = models.CharField(max_length=128)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    now = datetime.datetime.now
    title = models.CharField(max_length=128, default="non title")
    text = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
