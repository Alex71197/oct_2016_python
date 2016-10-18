from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
        # Select * From Course
    }
    return render(request, 'course_app/index.html', context)

def create(request):
    #using ORM - Creating an Object inside Course
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    print Course.objects.all()
    # Using the Insert in MySQL
    return redirect('/')

def destroy(request, id):
    course_delete = Course.objects.get(id = id)
    return render(request, 'course_app/destroy.html', { 'course' : course_delete })

def confirm_destroy(request, id):
    Course.objects.get(id = id).delete()
    return redirect('/')
