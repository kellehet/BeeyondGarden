from django.db import models

# Create your models here.
class Service(models.Model):
    type = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50, blank=True)
    icon = models.CharField(max_length=20, blank=True)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField(max_length=5000)

    def __str__(self):
        return self.type
