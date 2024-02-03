from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout
from closet.models import ClosetClothes
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Username and password are required.")
    
    return render(request, "login.html")
    

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email already used")
                return redirect("register")
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username = username,email = email,password= password)
                user.save();
                return redirect("/")
        else:
            messages.info(request,"Passwords are not same")
            return redirect("register")
    else:    
        return render(request, "register.html")
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")  


@login_required
def profile(request):
    user_id2 = request.user.id
    clothes = len(ClosetClothes.objects.filter(user_id = user_id2))
    user = get_object_or_404(User, id=user_id2)
    return render(request,"profile.html",{"user": user,"clothes_count":clothes,})