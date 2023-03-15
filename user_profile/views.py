from django.shortcuts import render,redirect
from user_home.models import CustomUser
from .models import User_Address
from .forms import AddressForm
from django.contrib import messages

def user_profile(request):
    context = {
        'address':User_Address.objects.filter(user=request.user),
    }
    return render(request,'user_profile/user_profile.html',context)

def change_dp(request):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)

    try:
        image = request.FILES['user_image']
        user.user_image=image
        user.save()
    except:
        pass
       
    return redirect(user_profile)

def edit_address(request, address_id):
    address =User_Address.objects.get(id=address_id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(user_profile)
    else:
        form = AddressForm(instance=address)
    
    return render(request, 'user_profile/edit_address.html', {'form': form})

def edit_profile(request):

    def validateEmail( email ):
        from django.core.exceptions import ValidationError
        from django.core.validators import validate_email
        try:
            validate_email( email )
            return True
        except ValidationError:
            return False

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    check = [name,email,phone]
    for values in check:
        if values == '':
            messages.info(request,'some fields are empty')
            return redirect(user_profile)
        else:
            pass

    if not validateEmail(email):
        messages.info(request,'Please enter valid email address')
        return redirect(user_profile)

    user_id = request.user.id
    usr = CustomUser.objects.filter(id = user_id)

    usr.update(username = name, email = email, phone = phone)

    return redirect(user_profile)

def add_address(request):

    address = User_Address.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect(user_profile)
    else:
        form = AddressForm()
    return render(request,'user_profile/add_address.html',{'form':form})

def delete_address(request,address_id):
    User_Address.objects.get(id=address_id).delete()
    return redirect(user_profile)

