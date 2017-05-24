import random
import string
from django.db import models

# Create your models here.
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class armURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("Something")
        self.shortcode = code_generator()
        super(armURL, self).save(*args, **kwargs)


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