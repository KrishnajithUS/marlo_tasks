from django.urls import path
from .views import home_page,auth_material_display
from django.views.generic.base import TemplateView

urlpatterns = [
# path('',TemplateView.as_view(template_name = 'home/home.html')),
path('',auth_material_display,name='auth_material_display'),

path('home/',home_page,name='post_user_review'),
]