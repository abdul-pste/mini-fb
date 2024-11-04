from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView, View
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm, Image, UpdateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            form.instance.user = user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

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
        # Save the status message
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        sm = form.save(commit=False)  # Save the form but don't commit yet
        sm.profile = profile
        sm.save()

        # Handle file uploads
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image(image_file=file, status_message=sm)  # Associate image with status message
            image.save()

        return redirect('show_profile', pk=profile.pk)
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_success_url(self):
        # Redirect to the updated profile page
        return reverse('show_profile', kwargs={'pk': self.object.pk})
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    

class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    fields = ['message']
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self):
        # Ensure that the profile's pk is passed correctly
        profile = self.object.profile  # Access the related Profile object
        return reverse('show_profile', kwargs={'pk': profile.pk})

class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'

    def get_success_url(self):
        profile = self.object.profile  # Access the related Profile object
        return reverse('show_profile', kwargs={'pk': profile.pk})
    
class CreateFriendView(View):
    def dispatch(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        other = get_object_or_404(Profile, pk=kwargs['other_pk'])
        profile.add_friend(other)
        return redirect('show_profile', pk=profile.pk)



class ShowFriendSuggestionsView(DetailView):
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suggested_friends'] = self.object.get_friend_suggestions()
        return context
    


class ShowNewsFeedView(DetailView):
    model = Profile
    template_name = 'mini_fb/news_feed.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_feed'] = self.object.get_news_feed()
        return context