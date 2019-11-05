from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url('', TemplateView.as_view(template_name='index.html')),
    url('/upload_file', views.upload_file, name="upload"),
    url('/uploadFile', views.upload_file, name="upload")
]