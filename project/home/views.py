from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from home.models import Employees

# Create your views here.
@login_required(login_url='/login')
def home(request):
    emp = Employees.objects.all()


    context = {'emp':emp}
    return render(request,'base/home.html',context)


def add(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(name=name,email=email,address=address,phone=phone)

        emp.save()

        return redirect('home')
    return render(request,'base/home.html',context)

def edit(request):
    emp = Employees.objects.all()


    context = {'emp':emp}
    return render(request, context)

def update(request,id):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(id=id,name=name,email=email,address=address,phone=phone)

        emp.save()

        return redirect('home')
    return render(request,'base/home.html',context)

def delete(request,id):

    emp = Employees.objects.filter(id = id)

    emp.delete()
    return redirect('homed')

def registerPage(request):
    page = 'register'

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')


    context = {'form': form}
    return render(request, 'base/login.html',context)

def login_reg(request):
    page = 'login'

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request, 'Username or password is wrong')
    context = {'page':page}
    return render(request, 'base/login.html',context)

def log_out(request):

    logout(request)
    return redirect('home')

    