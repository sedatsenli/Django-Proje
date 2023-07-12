from django.shortcuts import render 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout

def login_request(request):
     if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         
         user = authenticate(request, username = username, password = password)
         
         if user is not None:
             login(request, user)
             return redirect("indexx")
         else:
             return render(request, "login.html", {
                 "error": "kullanıcı adı veya parola yanlış"
             })

     return render(request, "login.html")

def signup_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"signup.html", {"error":"Kullanıcı adı kullanılıyor."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "signup.html", {"error":"E-posta kullanılıyor."})
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request,'signup.html', {"error": "Parola eşleşmiyor."})
    
    return render(request, "signup.html")
        
def logout_request(request):
    logout(request)
    return redirect(request, "login.html")
