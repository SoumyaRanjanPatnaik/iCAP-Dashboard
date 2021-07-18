from os import stat
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def ajax(request):
    status = "error"
    if(request.method == "POST"):
        body_raw = request.body
        json_body = json.loads(body_raw)
        status = "OK"
    return JsonResponse({"status":status, "request val": json_body})

@csrf_exempt
def ajax_GET(request):
    raise PermissionDenied