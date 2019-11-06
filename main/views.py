from django.shortcuts import  render,HttpResponse,redirect
from .models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from django.middleware.csrf import get_token, rotate_token

# Create your views here.
@require_http_methods(["GET", "POST"])
def upload_file(request):
    print("upload_file")
    response = {}
    try:
        if request.method == "GET":
            print(111)
            get_token(request)
        if request.method == "POST":
            print(request.body)
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    # data = request.FILES.get('file')
    # create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # # SaveFile.objects.create(create_time=create_time, file_url=data)
    # # return render_json({"result": True})