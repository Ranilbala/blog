from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    data = models.CharField(max_length=1000000)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
