from django.db import models

class BoardData(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=10)
