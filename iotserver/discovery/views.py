from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
import json

# Create your views here.

def index(request):
    #return HttpResponse('Got to index View')
    return render(request, 'discovery/room.html', {
        'room_name_json': mark_safe(json.dumps('discovery'))
    })


