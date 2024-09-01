from django.http import HttpResponse
from django.shortcuts import render

def show_products(request):
    return render(request, "products1/homepage.html", {})




from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout









def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST['fname']
            user.last_name = request.POST['lname']
            user.email = request.POST['email']
            user.save()
            auth_login(request, user)  
            return redirect('home')  
        else:
            return HttpResponse("Form is not valid")
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, "products1/signup_page.html", {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home') 
        else:
            return HttpResponse("Invalid credentials")
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, "products1/login_page.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  







