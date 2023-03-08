from django.shortcuts import render,redirect
from django.contrib import messages,auth


def admin_login(request):
    if request.user.is_superuser:
        return redirect(admin_home)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                auth.login(request,user)
                return redirect(admin_home)
            else:
                messages.error(request,f"{user} is not have admin access")
                return redirect(admin_login)
        else:
            messages.info(request,'credential mismatch')
            return redirect(admin_login)
    else:
        return render(request,'admin_home/admin_login.html')

def admin_logout(request):
    auth.logout(request)
    return redirect(admin_login)

def admin_home(request):
    if not request.user.is_superuser:
        return redirect(admin_login)
    return render(request,'admin_home/admin_home.html')

def admin_orders(request):
    return render(request,'admin_home/admin_orders.html')

def admin_profile(request):
    return render(request,'admin_home/admin_profile.html')

def admin_offers(request):
    return render(request,'admin_home/admin_offers.html')
    