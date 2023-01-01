from django.shortcuts import render, redirect
from .forms import RiderForm, RequesterForm
from .models import Requester, Rider


def rider_create_view(request):
    form = RiderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/riders')
    context = {
        'form': form
    }
    return render(request, 'riders/create.html', context)


def rider_list_view(request):
    riders = Rider.objects.all()
    context = {
        'riders': riders
    }
    return render(request, 'riders/list.html', context)


def requester_create_view(request):
    form = RequesterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/requesters')
    context = {
        'form': form
    }
    return render(request, 'requesters/create.html', context)


def requester_list_view(request):
    requesters = Requester.objects.all()
    context = {
        'requesters': requesters
    }
    return render(request, 'requesters/list.html', context)

