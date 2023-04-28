from django.contrib import admin
from .models import User, UserReview, Category, Material
# Register your models here.
admin.site.register(User)
admin.site.register(UserReview)
admin.site.register(Category)
admin.site.register(Material)