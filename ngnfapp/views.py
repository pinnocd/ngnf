# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def howitworks(request):
    return render(request, 'howitworks.html')

def successes(request):
    return render(request, 'successes.html')

def contact(request):
    return render(request, 'contact.html')

