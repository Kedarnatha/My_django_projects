from django.shortcuts import render

def index(request):
    return render(request,'index.html')
# Create your views here.
def myfirstpage(request):
    return render(request,'index.html')

def secondpage(request):
    return render(request,'second.html')