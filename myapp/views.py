from django.shortcuts import render

def index(request):
    return render(request,'index.html')
# Create your views here.
def myfirstpage(request):
    return render(request,'index.html')

def secondpage(request):
    return render(request,'second.html')

def thirdpage(request):
    var="Hello, Kedar! "
    greeting="Hey Kedar How are you doing "
    fruits=["apple","banana","mango","orange"]
    num1,num2=20,10
    ans=num1>num2
    dictinory={
        "var":var,
        "msg": greeting,
        "fruits":fruits,
        "num1":num1,
        "num2":num2,
        "results":ans
    }
    return render(request,'third.html',context=dictinory)
def myimage(request):
    return render(request,'image.html')
