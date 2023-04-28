from django.shortcuts import render
from api.models import UserReview,Material
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from .decorators import is_user_authenticated
# Create your views here.

def home_page(request):
    print(request.POST,"the ajax data")
    if request.method == 'POST' and request.is_ajax():

        email = request.POST.get('email')
        password = request.POST.get('password')
        print("email",email,password)
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            print(request.user,'user details')
            return JsonResponse({"success":"successfully logged in"},status=200)
        else:
            errors = {"errors":"invalid credentials"}
            return JsonResponse({"errors":errors},status=400)
    material = Material.objects.all()
    print(material)
    context ={
        'material':material
    }
    return render(request,'home/home.html',context)
@is_user_authenticated()
def auth_material_display(request):
        material_items = UserReview.objects.filter(user = request.user)
        return JsonResponse({"material":material_items})




