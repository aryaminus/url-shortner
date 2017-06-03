from django.db import models

# Create your models here.

from shortener.models import armURL

class ClickEvent(models.Model):
    arm_url    = models.OneToOneField(armURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{i}".format(i=self.count) 