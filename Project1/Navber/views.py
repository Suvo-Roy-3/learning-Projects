from django.shortcuts import render

def About(request):
    return render(request,'Navber/about.html')

def contact(request):
    return render(request,'Navber/contact.html')