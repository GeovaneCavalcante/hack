from django.shortcuts import render
from super.forms import MeuFrom
from django.http import HttpResponseRedirect
from super.models import Dados

def index(request):
    if request.method == 'POST':
        form = MeuFrom(request.POST)
        if form.is_valid():
            q = Dados()
            q.email = form.data.get('email')
            q.senha = form.data.get('senha')
            q.quantidade = form.data.get('quanti')
            q.save()
            return HttpResponseRedirect('/')
    else:
        form = MeuFrom()
    return render(request, 'index.html', {'form':form})
