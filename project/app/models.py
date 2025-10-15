from django.db import models

# Create your models here.
class ProcessedFile(models.Model):
    name = models.CharField()
    processed_content = models.CharField()