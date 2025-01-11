from django.shortcuts import render
from .models import Student
from .forms import StudentForm
# Create your views here.
def show(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            # print(fm.cleaned_data)
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # pw=fm.cleaned_data['password']
            # st=Student(name=nm,email=em,password=pw)
            # st.save()
            fm.save()
            # return render(request,'enroll/home.html',{'form':fm.cleaned_data})
    else:
        fm=StudentForm()
    return render(request,'enroll/home.html',{'form':fm})


def addshow(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            # print(fm.cleaned_data)
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # pw=fm.cleaned_data['password']
            # st=Student(name=nm,email=em,password=pw)
            fm.save()
            fm=StudentForm()

                # return render(request,'enroll/home.html',{'form':fm.cleaned_data})
    else:
            stu=Student.objects.all()
            fm=StudentForm()
    return render(request,'enroll/addshow.html',{'form':fm,'stud':stu})


def update(request):

    return render(request,'enroll/update.html')
