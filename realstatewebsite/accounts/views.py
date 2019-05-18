from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        #Register logic
        messages.error(request, "Testing Error MESSAGE")
        return redirect("register")
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        #login logic
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
