from django.db import models

# Create your models here.
class ToDo(models.Model):
    tasks= models.CharField(max_length=200)
    completed= models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


