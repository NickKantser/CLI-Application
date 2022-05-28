from django.shortcuts import render, get_object_or_404
from .models import File
import mimetypes
import os

class FileMetaData:
    file = None
    filename = None
    mimetype = None
    created_at = None
    size = None

    def set_file(self, uuid):
        self.file = get_object_or_404(File, pk=uuid)
        self.filename = os.path.basename(self.file.file.name)
        self.mimetype = mimetypes.guess_type(self.file.file.name)[0]
        self.created_at = self.file.created_at
        self.size = self.file.file.size

    def get_meta_data(self):
        context = { 'created_at': self.created_at,
                    'size': self.size,
                    'mimetype': self.mimetype,
                    'name': self.filename,
                    }

        return context

# def get_file_meta_data(uuid):
#     file = get_object_or_404(File, pk=uuid)
#     filename = os.path.basename(file.file.name)
#     mimetype = mimetypes.guess_type(file.file.name)[0]
#
#     context = { 'created_at': file.created_at,
#                 'size': file.file.size,
#                 'mimetype': mimetype,
#                 'name': filename,
#                 }
#
#     return context
