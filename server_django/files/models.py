from django.db import models

class File(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.PositiveIntegerField()
    mimetype = models.CharField(max_length=30)
    file = models.FileField(upload_to='media/%Y/%m/%d/')
