from django.shortcuts import render, redirect
import random
import time
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'gold/index.html')

def getgold(request):
    buildings = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }
    if request.method == "POST":
        date = time.strftime(' %m/%d/%Y --- %H:%M:%S %p')
        if request.POST['building'] in buildings:

            gold_added = buildings[request.POST['building']]
            request.session['gold'] += gold_added
            not_casino = "Earned {} gold from the {}".format(gold_added, request.POST['building'])
            casino = "You entered a casino and {} {} gold!".format("won" if gold_added > 0 else "lost", gold_added if gold_added > 0 else -gold_added)
            activity_content = {
                'activity': not_casino if request.POST['building'] != 'casino' else casino,
                'date': date
            }
            request.session['activity'].append(activity_content)
            print request.session['activity']
            print not_casino
    return redirect(index)

def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')
