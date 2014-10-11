from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import ListObject
from datetime import datetime



def index_view(request):
    return render(request, 'trolis/index.html', {})

def vomax_view(request):
    kontekstas = {'vardai': ['Vita', 'Evalina']}
    kontekstas['vardai'].append('Lina')
    return render(request, 'trolis/vomax.html', kontekstas)

def trolis_view(request):
    message = ''
    if request.POST:
        if request.user.is_authenticated():
            logout(request)
        else:
            if not request.POST.get('username') or not request.POST.get('password'):
                message = u'Your username or password was entered incorrectly'
            else:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
    return render(request, 'trolis/trolis.html', {
        'list_objects': ListObject.objects.all(),
        'message': message,
        'time': datetime.now(),
    })

def checkers_view(request):
    checkers_table_squares = []
    for i in range(8):
        row = []
        for j in range(8):
            c = i + j
            color = 'white'
            if c % 2 == 1:
                color = 'black'
            checker = ''
            if color == 'black':
                if i < 3:
                    checker = 'w'
                if i > 4:
                    checker = 'b'
            row.append({'x': 52*i, 'y': 52*j, 'c': color, 'checker': checker})
        checkers_table_squares.append(row);
    return render(request, 'trolis/checkers.html', {'coord': checkers_table_squares})

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
