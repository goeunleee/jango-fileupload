from django.shortcuts import render, get_object_or_404, redirect
from .models import Cloud
from datetime import date
# Create your views here.

def upload_cloud(request):
    if request.method =="POST":
        subject = request.POST['subject']
        file = request.FILES['file']
        filetype = request.POST['filetype']
        description = request.POST['description']
        try:
            Cloud.objects.create(uploadingdate=date.today(),subject=subject,file=file,filetype=filetype,description=description)
        except:
            pass 
    cloud = Cloud.objects.all()
    return render(request, 'upload_cloud.html',{'cloud':cloud})    
