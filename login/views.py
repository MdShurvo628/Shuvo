from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# def login(request):
#     if request.method == "POST":
#         email_input = request.POST.get('email')
#         password_input = request.POST.get('password')
#         user = User.objects.get(email=email_input)
#         if user.password == password_input:
#             return HttpResponse(f"Youre Logged In {user.fname} {user.lname} The Id is {user.id}")
#         else:
#             return HttpResponse(f"Wrong Password")

#     else:
#         return render(request, "login/login_page.html", {})

# def signup(request):
#     pwd= "Nothing"
#     if request.method == "POST":
#         form = UserEntry(request.POST or None)
#         if form.is_valid():
#             user = form.save()
#             user.fname = request.POST['fname']
#             user.lname = request.POST['lname']
#             user.username = request.POST['username']
#             user.email = request.POST['email']
#             pwd = make_password(request.POST['password'])
#             user.password = pwd
#             user.save()
#         return render(request, "login/test.html", {'pwd':pwd})
#     else:
#         return render(request, "login/test.html",{'pwd':pwd})





def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = request.POST['fname']
            user.last_name = request.POST['lname']
            user.email = request.POST['email']
            user.save()
            auth_login(request, user)  # Log in the user immediately after registration
            return redirect('home')  # Redirect to the home page or another page
        else:
            return HttpResponse("Form is not valid")
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, "login/signup_page.html", {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page or another page
        else:
            return HttpResponse("Invalid credentials")
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = AuthenticationForm()
            return render(request, "login/login_page.html", {'form': form})


def logout_view(request):
    """Log out the user and redirect to the homepage."""
    logout(request)
    return redirect('home')  # Redirect to home or login page

# def signup(request):
#     return render(request, "login/signup_page.html", {'form': form})



# def login_view(request):
#     return render(request, "login/login_page.html", {})
