from django.shortcuts import render
from .forms import RegisterForm,User
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    form=RegisterForm()
    return render(request,'register.html',{'form':form})


