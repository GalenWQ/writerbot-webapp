from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')

def write(request):
    return render(request, 'webapp/write.html')