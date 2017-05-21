from django.db import models

# Create your models here.
class armURL(models.Model):
    url = models.CharField(max_length=220, )

    def _str_(self):
        return str(self.url)
    
    def _unicode_(self):
        return str(self.url)