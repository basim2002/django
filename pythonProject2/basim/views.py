from django.shortcuts import render

# Create your views here.
def index1(request):
    return render(request,'index1.html')
def hello(request):
    return render(request,'hello.html')
def hi(request):
    return render(request,'aslam.html')
