from django.shortcuts import render

def home(request):
    return render(request, "htmlfiles/authorization.html")


def reset_password(request):
    return render(request, "htmlfiles/forgot.html")

def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, "htmlfiles/okroshka.html")  # Укажите путь к вашему шаблону


def page2(request):
    return render(request, "htmlfiles/profile.html")
