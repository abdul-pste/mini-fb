from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    UpdateProfileView, DeleteStatusMessageView, UpdateStatusMessageView,
    CreateFriendView, ShowFriendSuggestionsView, ShowNewsFeedView,
    ProfileListView, ShowAllProfilesView, ShowProfilePageView,
    CreateProfileView, CreateStatusMessageView
)

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile_list'), 
    path('base.html', views.home),
    path('', views.home, name='home'),
    path('show_all_profiles/', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
    path('status/create_status/', CreateStatusMessageView.as_view(), name='create_status'),
    path('status/<int:pk>/update/', UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', DeleteStatusMessageView.as_view(), name='delete_status'),

    path('profile/add_friend/<int:other_pk>/', CreateFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions/', ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),
    path('profile/news_feed/', ShowNewsFeedView.as_view(), name='news_feed'),

    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]
