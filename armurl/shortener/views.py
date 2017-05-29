from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import armURL

from django.shortcuts import render

# Create your views here.

def arm_redirect_view(request, shortcode=None, *args, **kwargs):
    try:
        obj = armURL.objects.get(shortcode=shortcode)
    except:
        obj = armURL.objects.all().first()
    
    qs = armURL.objects.filter(shortcode_iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
    return HttpResponse("YO {sc}".format(sc= obj.url))

class ArmCBView(View):
    def get(self,request, shortcode=None, *args, **kwargs):
        return HttpResponse("Yo Yo {sc}".format(sc= shortcode))