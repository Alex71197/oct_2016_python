from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    print request.session['count']
    request.session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
    return render(request, 'randomword/index.html')

def generate(request):
    print request.method
    if request.method == "POST":
        print request.POST
        return redirect('/')
