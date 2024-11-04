from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image_url = models.URLField()

    def get_status_messages(self):
        # Returns all status messages related to this profile
        return self.statusmessage_set.all().order_by('-timestamp')
    
    def get_friends(self):
        friends1 = Friend.objects.filter(profile1=self).values_list('profile2', flat=True)
        friends2 = Friend.objects.filter(profile2=self).values_list('profile1', flat=True)
        friend_ids = list(friends1) + list(friends2)
        return Profile.objects.filter(id__in=friend_ids)
    
    def add_friend(self, other):
        if self == other:
            return  # Prevent self-friending
        if not Friend.objects.filter(profile1=self, profile2=other).exists() and not Friend.objects.filter(profile1=other, profile2=self).exists():
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestions(self):
        friends = self.get_friends()
        excluded_profiles = [friend.pk for friend in friends] + [self.pk]
        return Profile.objects.exclude(pk__in=excluded_profiles)

    def get_news_feed(self):
        friends = self.get_friends()
        friend_ids = [friend.pk for friend in friends] + [self.pk]
        return StatusMessage.objects.filter(profile__pk__in=friend_ids).order_by('-timestamp')



class StatusMessage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]
    
class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    status_message = models.ForeignKey('StatusMessage', on_delete=models.CASCADE, related_name='images')
    timestamp = models.DateTimeField(default=timezone.now)


class Friend(models.Model):
    profile1 = models.ForeignKey(Profile, related_name="profile1", on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name="profile2", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.profile1} & {self.profile2}"

