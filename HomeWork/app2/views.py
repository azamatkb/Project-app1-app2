from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    renthouse = Renthouse.objects.all()
    context = {
        'renthouse' : renthouse,
    }
    return render(request, template_name='app2/index.html', context=context)
