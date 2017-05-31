from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import armURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {}) 
        
    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.POST["url"])
        print(request.POST.get("url"))
        return render(request, "shortener/home.html", {})

class ArmCBView(View):
    def get(self,request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(armURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)