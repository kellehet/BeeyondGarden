from django.db import models
from services.models import Service
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=50, default='picture')
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title



