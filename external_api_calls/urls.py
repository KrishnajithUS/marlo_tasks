from django.urls import path
from . import views


urlpatterns = [

 path('create-product-crud/',views.CurdCurdApi.as_view()),
 path('create-product-crud/<str:id>', views.CurdCurdApi.as_view())

]


