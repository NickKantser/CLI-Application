from django.shortcuts import render
from django.http import HttpResponse

def stat(request, uuid):
    res = f'This is filemeta of the {uuid}th file'
    return HttpResponse(res)

def read(request, uuid):
    res = f'This is the content of the {uuid}th file'
    return HttpResponse(res)
