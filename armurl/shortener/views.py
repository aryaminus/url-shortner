from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.shortcuts import render

# Create your views here.

def arm_redirect_view(request, *args, **kwargs):
    return HttpResponse("YO")

class ArmCBView(View):
    def get(self,request, *args, **kwargs):
        return HttpResponse("Yo Yo")