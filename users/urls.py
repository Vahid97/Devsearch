from django.urls import path

from projects.views import updateProject
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edi-account/', views.editAccount, name='edit-account'),
    path('create-skill/', views.createSkill, name='create-skill'),
    path('update-skill/', views.updateSkill, name='update-skill'),
    path('delete-skill/', views.updateSkill, name='delete-skill'),
]