from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('<int:city_id>/', views.city_dashboard),
    path('profile/<int:user_id>/', views.show_profile),
    path('new/', views.new_activity),
    path('show/<int:activity_id>/', views.show_activity),
    path('edit/<int:activity_id>/', views.edit_activity),
    path('about/', views.about_us),
]