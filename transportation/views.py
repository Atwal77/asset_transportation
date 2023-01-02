from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import RiderForm, RequesterForm, TransportationRequestForm
from .models import Requester, Rider, TransportationRequest


def rider_create_view(request):
    form = RiderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/transportation/riders')
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
        return redirect('/transportation/requesters')
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

def rider_match_list_view(request,**kwargs):
    # Get the requester object based on the authenticated user
    requester_email_id = kwargs['email_id']
    requester = Requester.objects.get(email_id=requester_email_id)
    # Get the asset transportation request created by the requester
    transportation_request = TransportationRequest.objects.filter(requester=requester).first()
    # Get the matching travel info shared by Riders
    riders = Rider.objects.filter(from_location=transportation_request.from_location,
                                  to_location=transportation_request.to_location)
    # Render the template with the matching Rider objects and the transportation request object
    return render(request, 'riders/match_list.html', {'riders': riders, 'transportation_request': transportation_request})

def rider_details_view(request, rider_id):
    rider = Rider.objects.get(id=rider_id)
    data = {
        'id': rider.id,
        'from_location': rider.from_location,
        'to_location': rider.to_location,
        'assets': rider.assets,
    }
    return JsonResponse(data)

def create_transportation_request(request):
    # Initialize form with POST data
    form = TransportationRequestForm(request.POST)

    # Validate form data
    if form.is_valid():
        # Save TransportationRequest object from form data
        transportation_request = form.save()
        return redirect('/transportation/request')

    context = {
        'form': form
    }
    return render(request, 'transportation_request/create.html', context)