from django.db import models
from django.utils import timezone

# Create your models here.
class Cloud(models.Model):
    uploadingdate = models.DateField(auto_now=True)
    subject = models.CharField(max_length=50, null=True)
    file = models.FileField(null=True)
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.subject


