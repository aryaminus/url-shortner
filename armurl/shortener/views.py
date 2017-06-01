from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm

from .models import armURL

def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        return render(request, "shortener/home.html", {}) 

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        return render(request, "shortener/home.html", {})

class ArmCBView(View):
    def get(self,request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(armURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)