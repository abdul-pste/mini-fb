from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.profile_list, name='profile_list'),
    path('base.html', views.home),
    path('', views.home, name='home'),
    path('show_all_profiles/', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/create_status/', views.CreateStatusMessageView.as_view(), name='create_status'),
]

