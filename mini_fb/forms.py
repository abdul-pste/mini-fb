from django import forms
from .models import Profile, StatusMessage, Image

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'profile_image_url']

class CreateStatusMessageForm(forms.ModelForm):
    class Meta:
        model = StatusMessage
        fields = ['message']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file']
