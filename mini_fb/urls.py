from django.urls import path
from . import views



urlpatterns = [
    path('profiles/', views.profile_list, name='profile_list'),
    path('', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
]
