from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import File
import mimetypes
import os

def stat(request, uuid):
    file = get_object_or_404(File, pk=uuid)
    filename = os.path.basename(file.file.name)
    mimetype = mimetypes.guess_type(file.file.name)[0]
    context = { 'created_at': file.created_at,
                'size': file.file.size,
                'mimetype': mimetype,
                'name': filename,
                }
    return JsonResponse(context)

def read(request, uuid):
    res = f'This is the content of the {uuid}th file'
    return HttpResponse(res)
