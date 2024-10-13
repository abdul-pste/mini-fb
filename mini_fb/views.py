from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Profile
# Create your views here.



# Function-based view for the profile list
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'mini_fb/profile_list.html', {'profiles': profiles})

# Function-based view for the home page
def home(request):
    return render(request, 'mini_fb/base.html')  # Specify the template here


class ShowAllProfilesView(ListView):
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'