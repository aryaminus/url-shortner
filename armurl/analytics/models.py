from django.db import models


from shortener.models import armURL

class ClickEventManager(models.Manager):
    def create_event(self, armInstance):
        if isinstance(armInstance, armURL):
            obj, created = self.get_or_create(arm_url=armInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    arm_url    = models.OneToOneField(armURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count) 