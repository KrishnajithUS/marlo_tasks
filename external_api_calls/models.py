from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=80)
    price = models.IntegerField()