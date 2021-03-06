from home.models import Worker
from json.encoder import JSONEncoder
from os import stat
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import time
import json
from . import userfunc 
from home.models import Worker

# Create your views here.
def index(request):
    workers = Worker.objects.all()
    context={"title":"Dashboard", "dash_class":"active", "logs_class":"", "att_class":"","about_class":"", "worker_list":workers}
    return render(request, 'index.html', context)

def attendence(request):
    workers = Worker.objects.all()
    context={"title":"Attendance", "dash_class":"", "logs_class":"", "att_class":"active","about_class":"", "worker_list":workers}
    return render(request, 'attendance.html',context)

def logs(request):
    workers = Worker.objects.all()
    context={"title":"Logs", "dash_class":"", "logs_class":"active", "att_class":"","about_class":"", "worker_list":workers}
    return render(request, 'logs.html',context)

def about(request):
    context={"title":"About", "dash_class":"", "logs_class":"", "att_class":"","about_class":"active"}
    return render(request, 'about.html',context)

@csrf_exempt
def get(request):
    response_val = {}
    if(request.method == "GET"):
        if(request.GET.get("addr")):
            if(request.GET['addr']=='all'):
                response_val= userfunc.update_dashboard()
    return JsonResponse(response_val)
    

@csrf_exempt
def send(request):
    global WORKERS
    status = "[ERROR]"
    json_body = {}
    if(request.method == "POST"):
        body_raw = request.body
        json_body = json.loads(body_raw)
        if("addr" in json_body) and ("data" in json_body):
            status = "[OK]"
            address_val = json_body["addr"]
            if Worker.objects.filter(pk=address_val).exists():
                userfunc.update_model(json_body["data"], address_val)
            else:
                json_body="Invalid API KEY"
        else:
            json_body = "Invalid Request"
        print(json_body)
    return JsonResponse({"status":status, "reponse": json_body})
    