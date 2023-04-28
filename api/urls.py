from django.urls import path
from . import views
from rest_framework import routers
from .Routers import  CustomReadOnlyRouter
from rest_framework.schemas import  get_schema_view
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView
)
custom_router = CustomReadOnlyRouter()
router = routers.DefaultRouter()
custom_router.register('category',views.CategoryView)
router.register(r'sub-category-crud', views.SubCategoryView)
router.register(r'sub-category-crud/(?P<id>\d+/#$)', views.SubCategoryView)
router.register(r'create-user', views.CreateUser)
router.register(r'create-user/(?P<id>\d+/#$)', views.CreateUser)
router.register(r'create-user-review', views.CreateUserReview)
router.register(r'create-user-review/(?P<id>\d+/#$)', views.CreateUserReview)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path('schema', get_schema_view(
        title='rest',
        description='Api Documentation'
    ), name='openap-shcema')
]
urlpatterns += router.urls 
