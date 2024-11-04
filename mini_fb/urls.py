from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

from .views import UpdateProfileView, DeleteStatusMessageView, UpdateStatusMessageView, CreateFriendView, ShowFriendSuggestionsView, ShowNewsFeedView


urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('show_all_profiles/', views.ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='show_profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('status/create_status/', views.CreateStatusMessageView.as_view(), name='create_status'),
    path('status/<int:pk>/update/', views.UpdateStatusMessageView.as_view(), name='update_status'),
    path('status/<int:pk>/delete/', views.DeleteStatusMessageView.as_view(), name='delete_status'),
    path('profile/add_friend/<int:other_pk>/', views.CreateFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions/', views.ShowFriendSuggestionsView.as_view(), name='friend_suggestions'),
    path('profile/news_feed/', views.ShowNewsFeedView.as_view(), name='news_feed'),
    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]


