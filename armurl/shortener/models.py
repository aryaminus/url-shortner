from django.db import models

# Create your models here.
class armURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)