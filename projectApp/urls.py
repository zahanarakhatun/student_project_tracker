from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # কাস্টম লগইন ভিউ যুক্ত করা হলো
    path(
        'logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'
    ),
    path('projects/', views.project_list_view, name='project_list'),
    path('projects/add/', views.add_project_view, name='add_project'),
    path(
        'projects/update/<int:pk>/',
        views.update_status_view,
        name='update_status',
    ),
]