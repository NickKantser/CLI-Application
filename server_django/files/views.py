from django.http import JsonResponse, FileResponse
from django.views.generic import View
from .utils import FileMetaData

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
