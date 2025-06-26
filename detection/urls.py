from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='detection/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image_view, name='upload_image'),
    path('about/', views.about_view, name='about'),
    path('', views.home_view, name='home'),
]
