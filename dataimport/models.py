from django.db import models

class ImportedData(models.Model):
    data = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
