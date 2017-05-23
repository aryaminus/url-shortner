from django.db import models

# Create your models here.
class armURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

'''
 python manage.py makemigrations
 python manage.py migrate
 python manage.py flush 
 python manage.py createsuperuser
 
 python manage.py createsuperuser
'''