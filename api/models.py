from django.db import models

class User(models.Model):
    age  = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name