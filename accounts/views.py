from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('product:home')
    return render(request, 'accounts/login.html')

@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
        

def create_user(request):
    if request.method == "POST":

        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if password1 == password2:

            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
           
                
            return redirect('product:home')
    return render(request, 'accounts/register.html')

@login_required(login_url='accounts:login')
def edit_user(request,pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        
        user.save()
        
        return redirect('product:home')

    return render(request, 'users/edit.html', {'user': user})



@login_required(login_url='accounts:login')
def delete_user(request, pk):
    user = User.objects.get(pk=pk)

    user.delete()

    return redirect('product:home')

