from django.db import models
from account.models import MyUser

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=60, unique=True)


class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=80)


class User(models.Model):
    user_name = models.CharField(max_length=70, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=20)


class UserReview(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    review = models.CharField(max_length=80)
