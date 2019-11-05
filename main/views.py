from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import time

# Create your views here.
@csrf_exempt
def upload_file(request):
    print("1111")

    # data = request.FILES.get('file')
    # create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    # # SaveFile.objects.create(create_time=create_time, file_url=data)
    # # return render_json({"result": True})