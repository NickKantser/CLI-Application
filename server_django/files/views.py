from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, FileResponse
from .utils import FileMetaData
from .models import File
import os


from django.views.generic import View


# def stat(request, uuid):
#     file = get_object_or_404(File, pk=uuid)
#     filename = os.path.basename(file.file.name)
#     mimetype = mimetypes.guess_type(file.file.name)[0]
#     context = { 'created_at': file.created_at,
#                 'size': file.file.size,
#                 'mimetype': mimetype,
#                 'name': filename,
#                 }
#
#     return JsonResponse(context)

class StatView(View, FileMetaData):
    def get(self, request, *args, **kwargs):
        uuid = kwargs['uuid']
        self.set_file(uuid)
        context = self.get_meta_data()
        return JsonResponse(context)


class ReadView(View, FileMetaData):
    def get(self, request, *args, **kwargs):
        uuid = kwargs['uuid']
        self.set_file(uuid)
        response = FileResponse(open(self.file.file.path, 'rb'))

        return response


# def read(request, uuid):
#     uuid = kwargs['uuid']
#     self.set_file(uuid)
#     # file = get_object_or_404(File, pk=uuid)
#     # filename = os.path.basename(file.file.name)
#     # mimetype = mimetypes.guess_type(file.file.name)[0]
#     response = FileResponse(open(self.file.path, 'rb'))
#
#     return response
