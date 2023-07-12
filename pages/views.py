from django.shortcuts import render


# Create your views here.
def indexx(request):
    return render(request, 'indexx.html')

def contact(request):
    return render(request, 'contact.html')

#def login(request):
#   return render(request, 'login.html')

#def signup(request):
#    return render(request, 'signup.html')

def menu(request):
    return render(request, 'menu.html')

#def sepet(request):
 #   return render(request, 'sepet.html')

def today_special(request):
    return render(request, 'today-special.html')



