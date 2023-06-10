from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dat = 0
    data = {"int":dat}
    return render(request, "index.html", context=data)
def page(request):
    return render(request, "page.html") 
def about(request):
    return HttpResponse("<h2>about</h2>")
def contact(request):
    return HttpResponse("<h2>Contact</h2>") 
