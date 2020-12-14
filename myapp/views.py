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
    records = Record.objects.filter(user=user)
    return render(request, 'app/index.html', locals())


@login_required
def addEvent(request):
    if request.method == 'POST':
        user = request.user
        form = RecordForm(user, request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.save()
    return redirect('/')


@login_required
def deleteEvent(request):
    if request.method == 'POST':
        event_id = request.POST['delete_value']
        Record.objects.filter(id=event_id).delete()
    return redirect('/')


@login_required
def editEvent(request):
    if request.method == 'POST':
        event_id = request.POST['edit_value']
        record = Record.objects.get(id=event_id)

        return render(request, 'app/edit_event.html', locals())
    return redirect('/')


@login_required
def updateEvent(request):
    if request.method == 'POST':
        user = request.user
        posted_data = request.POST
        event_id = posted_data['id_value']
        date = posted_data['date']
        time_start = posted_data['time_start']
        time_end = posted_data['time_end']
        title = posted_data['title']
        description = posted_data['description']
        Record.objects.filter(id=event_id).update(date=date, time_start=time_start, time_end=time_end, title=title,
                                                  description=description)
    return redirect('/')


@login_required
def searchEvent(request):
    if request.method == 'POST':
        title = request.POST['title']
        user = request.user
        records = Record.objects.filter(user=user, title=title)
        return render(request, 'app/search_event.html', locals())
    return redirect('/')


@login_required
def shareEvent(request):
    if request.method == 'POST':
        event_id = request.POST['share_value']
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            record = Record.objects.get(id=event_id)
            Record.objects.create(date=record.date, time_start=record.time_start, time_end=record.time_end, title=record.title,
                                  description=record.description, user=user)
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
