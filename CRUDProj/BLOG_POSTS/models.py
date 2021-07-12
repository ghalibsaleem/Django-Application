from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class PostModel(models.Model):
    date = models.DateTimeField(default=timezone.now())
    txt = models.TextField(max_length=1000)
    title = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    

   
