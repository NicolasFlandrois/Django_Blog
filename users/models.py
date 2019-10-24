from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Add here more field (added on top of User's model) to appear in profile e.g. Bio, City, langage, etc

    def __str__(self):
        return f'{self.user.username} Profile'
