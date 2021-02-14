from django.shortcuts import render

# Create your views here.
from core.models import Eventos

def lista_eventos(request):

    evento = Eventos.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)








