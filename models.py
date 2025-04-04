from django.db import models
import uuid


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  

    class Mate:
        abstract = True
        ordering = ['-created_at']