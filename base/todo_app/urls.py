
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register_user, name="register"),
    path('info/<int:pk>/', views.user_task, name="info"),
    path('delete/<int:pk>', views.delete_task, name="delete"),
    path('add_task/', views.add_task, name="add_task"),
    path('update/<int:pk>', views.update_task, name="update")
]