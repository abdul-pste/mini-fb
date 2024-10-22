from django.urls import path
from . import views

from .views import UpdateProfileView, DeleteStatusMessageView, UpdateStatusMessageView


urlpatterns = [
    path('profiles/', views.profile_list, name='profile_list'),
    path('base.html', views.home),
    path('', views.home, name='home'),
    path('show_all_profiles/', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status/', views.CreateStatusMessageView.as_view(), name='create_status'),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('status/<int:pk>/update/', UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', DeleteStatusMessageView.as_view(), name='delete_status'),
]

