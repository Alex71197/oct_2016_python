from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
        print request.session['count']
    return render(request, 'form/index.html')

def session(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        print request.session['language']
        return redirect(result)

def result(request):
    return render(request, 'form/result.html')
