from django.shortcuts import render
from .forms import ThingForm

def home(request):

    # Instantiate an instance of ThingForm with initial data
    thingform = ThingForm()

    # Pass the form to the template context
    context = {
        'thingform': thingform,
    }

    return render(request, 'home.html', context)
