# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome To Home Page:")
def about(request):
    return HttpResponse("Know About This.... <a href='/'>BACk</a>")
def first(request):
    return HttpResponse("For more visit my web...<a href='/'>BACk</a>")
def link(request):
    return HttpResponse('''Click Here : <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> DJANGO VIDEOS </a>''')
def temp(request):
    var={'name':'SIBU','place':'kpda'}
    return render(request,'temp.html',var)



