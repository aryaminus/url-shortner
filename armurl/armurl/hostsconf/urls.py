from django.conf.urls import url
from django.contrib import admin

from shortener.views import arm_redirect_view, ArmCBView, test_view

from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?<path>.*)', admin.site.urls),
]