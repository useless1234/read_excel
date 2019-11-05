from django.db import models


# Create your models here.

class SaveFile(models.Model):
    create_time = models.DateTimeField(u"上传时间")
    file_url = models.FileField(upload_to='SavedExcel')
