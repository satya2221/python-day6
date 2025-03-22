from django.db import models
from .utils import generate_id
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default=generate_id, editable=False, max_length=100)
    actor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) #one to many dengan 1 user banyak record

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True