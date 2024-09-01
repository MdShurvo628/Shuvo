from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return render(request, "products1/show_product.html", {})
    return render(request, "products1/login_page.html", {})
    # return render(request,'login/homepage.html')



def about(request):
    return HttpResponse("Hello, world! From about!!! ")