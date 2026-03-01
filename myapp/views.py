from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def scenar(request):
    return render(request, 'scenar.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about_me.html')

def massage(request):
    return render(request, 'therapeutic_massage.html')

def reyki(request):
    return render(request, 'reyki_therapy.html')

def laser(request):
    return render(request, 'laser_therapy.html')