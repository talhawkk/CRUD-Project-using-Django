from django.shortcuts import render
from .models import Student
# Create your views here.
def show(request):

    return render(request,'enroll/home.html')


def addshow(request):

    return render(request,'enroll/addshow.html')

def update(request):

    return render(request,'enroll/update.html')
