from django.shortcuts import render
from app.forms import *
from django.core.files.storage import FileSystemStorage

# Create your views here.
def image(request):
    form=imageform()
    if request.method=="POST" and request.FILES:
        form_data=imageform( request.POST,request.FILES)
        if form_data.is_valid():
            img=form_data.cleaned_data['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
            image_url=fs.url(file)
            return render(request,'display_image.html',context={'image_url':image_url})


    return render(request,'imageform.html',context={'form':form})
