from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def ninja(request):
    return render(request, 'ninjas/ninja.html')

def color(request, ninjacolor):
    context = {
        'color': ninjacolor
    }
    return render(request, 'ninjas/color.html', context)
