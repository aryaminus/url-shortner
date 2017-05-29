from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import armURL

#from django.shortcuts import render

# Create your views here.

def test_view(request):
    return HttpResponse("Chaa Ching")

def arm_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(armURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class ArmCBView(View):
    def get(self,request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(armURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
    
    def post(self,request, *args, **kwargs):
        return HttpResponse()

   
    '''
    try:
        obj = armURL.objects.get(shortcode=shortcode)
    except:
        obj = armURL.objects.all().first()
    '''
    #obj_url = obj.url
    '''
    obj_url =None
    qs = armURL.objects.filter(shortcode_iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url
    '''