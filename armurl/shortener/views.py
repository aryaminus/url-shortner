from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import armURL

from django.shortcuts import render

# Create your views here.

def arm_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = armURL.objects.get(shortcode=shortcode)
    return HttpResponse("YO {sc}".format(sc= obj.url))

class ArmCBView(View):
    def get(self,request, shortcode=None, *args, **kwargs):
        return HttpResponse("Yo Yo {sc}".format(sc= shortcode))