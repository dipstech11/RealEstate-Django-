from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        #Register logic
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password check
        if password == password2:
            #username check
            if User.objects.filter(username=username).exists():
                #ERROR
                messages.error(request, "Username is taken")
                return redirect("register")
            else:
                #email
                if User.objects.filter(email=email).exists():
                    #ERROR
                    messages.error(request, "Email is taken")
                    return redirect("register")
                else:
                    ##all ok
                    #first way - direct Login
                    user = User.objects.create_user(username=username, password=password,email=email,
                                                    first_name=first_name, last_name=last_name)
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect("index")

                    #second way - register-login-home
                    user.save()
                    messages.success(request, "You are now registered and can login")
                    return redirect("login")
        else:
            messages.error(request, "Password didn't match")
            return redirect("register")
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        #login logic
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now Logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
