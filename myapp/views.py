from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import RecordForm, UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required
def index(request):
    user = request.user
    record_form = RecordForm(user=user)
    user_form = UserForm()
    records = Record.objects.filter(user=user, event_type='active')
    return render(request, 'app/index.html', locals())

@login_required
def addEvent(request):
    if request.method == 'POST':
        user = request.user
        form = RecordForm(user,request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.event_type = 'active'
            record.save()
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', locals())
