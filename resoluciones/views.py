from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Resoluciones

# Create your views here.

def resoluciones_all(request):
    misresoluciones = Resoluciones.objects.all().values()
    template = loader.get_template('resoluciones_all.html')
    context = {
        'misresoluciones': misresoluciones,
    }

    return HttpResponse(template.render(context, request))
