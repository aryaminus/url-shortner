from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, ArmCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+){6,15}/$', ArmCBView.as_view()), 
]
