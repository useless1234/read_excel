from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'first$', views.upload_file)
]