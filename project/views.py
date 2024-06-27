from django.shortcuts import render
from django.http import HttpResponse
# other imports
from .decorators import has_permission



# Create your views here.

@has_permission
def home(request):
    
    return HttpResponse(" Hellow Developer ")


@has_permission('retrive_job')
def job_list(request):
    # ...
    pass

@has_permission('update_project')
def project_edit(request):
    # ...
    pass

