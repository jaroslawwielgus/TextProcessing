from django.db import models

# Create your models here.
class ProcessedFile(models.Model):
    name = models.CharField(max_length=100)
    processed_content = models.TextField()