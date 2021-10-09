from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.
def images(request):

    images=Image.objects.all()
   

    return render(request,'images.html',{"images":images})