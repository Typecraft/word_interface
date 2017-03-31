from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=1000)
    freeTrans = models.CharField(max_length=1000)
    freeTrans2 = models.CharField(max_length=1000)
    comment = models.TextField()
