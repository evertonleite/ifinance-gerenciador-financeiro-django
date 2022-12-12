from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return redirect('login')
        
        user = User.objects.create_user(first_name=first_name, email=email,username=username, password=password)
        user.save()
        
        return HttpResponse('usuario cadastrado com sucesso')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return redirect('login')       

@login_required(login_url='ifinance/login/')
def home(request):
    return render(request, 'dashboard.html')

@login_required()
def logout(request):
    logout_django(request)
    return redirect('login')

@login_required()
def receita(request):
    return render(request, 'tables.html')

@login_required()
def despesa(request):
    return render(request, 'wallet.html')