from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.
def index(request):
    #instantiate default value for request.session['activities']
    if 'activities' not in request.session:
        request.session['activities'] = []

    # Instantiate default value for request.session['gold']
    if 'gold' not in request.session:
        request.session['gold'] = 0
    context = {
        'activities': request.session['activities'],
        'gold': request.session['gold'],
    }
    request.session.modified = True
    return render(request, "ninja/index.html", context)

def process_money(request):
    if request.method == 'POST':
        # find out which building was clicked on
        building = request.POST['building']

    if building == 'farm':
        amount = random.randint(10, 20)
        request.session['gold'] += amount
        request.session['activities'] = 'Earned', amount, 'golds from the farm'

    elif building == "cave":
        amount = random.randint(5, 10)
        request.session['gold'] += amount
        request.session['activities'] = 'Earned', amount, 'golds from the cave'

    elif building == 'house':
        amount = random.randint(2, 5)
        request.session['gold'] += amount
        request.session['activities'] = 'Earned', amount, 'golds from the house'

    elif building == 'casino':
        amount = random.randint(-50, 50)
        request.session['gold'] += amount
        if amount < 0:
            request.session['activities'] = 'You lost', amount, 'bad ninja'
        elif amount == 0:
            request.session['activities'] = '#You broke even go home'
        else:
            request.session['activities'] = 'Earned', amount, 'golds from the casino'
    return redirect("/")