
from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

def refresh_shortcodes(self):
    qs = KirrURL.objects.filter(id__gte=1)

class armURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)

    objects = KirrURLManager()
    #some_random = KirrURLManager()

    def save(self, *args, **kwargs):
        #print("Something")
        #self.shortcode = code_generator()
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
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
'''