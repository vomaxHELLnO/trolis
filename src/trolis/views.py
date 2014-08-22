from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import login

def index_view(request):
    return render(request, 'trolis/index.html', {})

def vomax_view(request):
    kontekstas = {'vardai': ['Vita', 'Evalina']}
    kontekstas['vardai'].append('Lina')
    return render(request, 'trolis/vomax.html', kontekstas)

def trolis_view(request):
    return render(request, 'trolis/trolis.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    #import ipdb; ipdb.set_trace()
    return render(request, 'trolis/login.html', {'form':form})
