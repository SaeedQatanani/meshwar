from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login_reg/', views.login_reg),
    path('add/', views.add_user),
    path('success/', views.render_success),
    path('logout/', views.log_out),
    path('login/', views.log_in),
    path('delete_all/', views.delete_all),
]