from django.db import models

class File(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name
