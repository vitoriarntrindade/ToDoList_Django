from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.http.response import Http404, JsonResponse


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def event(request):
    id_event = request.GET.get("id")
    data = {}
    if id_event:
        data['event'] = Event.objects.get(id=id_event)
    return render(request, 'event.html', data)


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')


@login_required(login_url='/login/')
def submit_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date_event = request.POST.get('date_event')
        description = request.POST.get('description')
        user = request.user
        id_event = request.POST.get('id_event')

        if not title or not date_event:
            return redirect('/')

        if id_event:
            try:
                event = Event.objects.get(id=id_event)
                if event.user == user:
                    event.title = title
                    event.description = description
                    event.event_date = date_event
                    event.save()
            except Exception:
                return redirect('/')
        else:
            Event.objects.create(title=title,
                                  event_date=date_event,
                                  description=description,
                                  user=user)
    return redirect('/')


@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    event = Event.objects.filter(user=user)
    data = {"event": event}
    return render(request, 'index.html', data)


@login_required(login_url='/login/')
def delete_event(request, id_event):
    user = request.user
    try:
        event = Event.objects.get(id=id_event)
    except Exception:
        raise Http404()
    if user == event.user:
        event.delete()
    else:
        raise Http404()
    return redirect('/')


def json_list_event(request):
    user = request.user
    event = Event.objects.filter(user=user).values('id', 'title')
    return JsonResponse(list(event), safe=False)