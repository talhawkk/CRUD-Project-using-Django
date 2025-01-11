from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def show(request):
    # if request.method=='POST':
    #     fm=StudentForm(request.POST)
    #     if fm.is_valid():
    #         # print(fm.cleaned_data)
    #         # nm=fm.cleaned_data['name']
    #         # em=fm.cleaned_data['email']
    #         # pw=fm.cleaned_data['password']
    #         # st=Student(name=nm,email=em,password=pw)
    #         # st.save()
    #         fm.save()
    #         # return render(request,'enroll/home.html',{'form':fm.cleaned_data})
    # else:
        # fm=StudentForm()
    return render(request,'enroll/home.html',)


def addshow(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
           
            fm.save()
            fm=StudentForm()

                # return render(request,'enroll/home.html',{'form':fm.cleaned_data})
    else:
            fm=StudentForm()
    stu=Student.objects.all()
    return render(request,'enroll/addshow.html',{'form':fm,'stud':stu})


def delete(request,id):
    if request.method=='POST':
        p=Student.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect('/')


def update(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
