from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name="home"),  # Добавьте этот маршрут
    path("login/", views.login_view, name="login"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("page2/", views.page2, name="profile"),
]
