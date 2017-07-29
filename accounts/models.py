from django.db import models
import datetime
import hashlib


class User(models.Model):
    now = datetime.datetime.now
    user_id = models.CharField(max_length=128, unique=True)
    user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False):
        self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
        super(User, self).save(force_insert, force_update)
