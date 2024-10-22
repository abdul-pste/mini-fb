from django.utils import timezone
from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image_url = models.URLField()

    def get_status_messages(self):
        # Returns all status messages related to this profile
        return self.statusmessage_set.all().order_by('-timestamp')

class StatusMessage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message[:50]}..." 
    
class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    status_message = models.ForeignKey('StatusMessage', on_delete=models.CASCADE, related_name='images')
    timestamp = models.DateTimeField(default=timezone.now)


