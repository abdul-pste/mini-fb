from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm



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


class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    

class CreateStatusMessageView(CreateView):
    model = StatusMessage
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        context['profile'] = profile
        return context

    def form_valid(self, form):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.instance.profile = profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.kwargs['pk']})