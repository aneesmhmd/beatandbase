from django.shortcuts import render,redirect
from user_home.models import CustomUser
from django.contrib import messages

def user_list(request):
    dict_user = {
        'users':CustomUser.objects.all().order_by('id')
    }
    return render(request,'user_management/user_list.html',dict_user)


def user_action(request,user_id):
    user = CustomUser.objects.get(id=user_id)
    print(user.is_active)
    if user.is_blocked:
        user.is_blocked=False
        user.save()
        print(user.is_blocked)
        return redirect(user_list)
    else:
        user.is_blocked=True
        user.save()
        return redirect(user_list)