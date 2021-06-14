from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    car = Cars.objects.all()
    context = {
        'car' : car,
    }
    return render(request, template_name='app1/index.html', context=context)
