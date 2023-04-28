from django.shortcuts import redirect
from django.urls import reverse

def is_user_authenticated():
    def wrapper(fun):
        def inner_wrapper(request):
                print(request.user)

                if request.user.is_authenticated:
                    return fun(request)
                else:
                    print("worked")
                    return redirect('post_user_review')
        return inner_wrapper
    return wrapper