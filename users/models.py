from PIL import Image
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# class User(AbstractUser):
#   phone_number = models.CharField(max_length=12)

class Profile(models.Model):
  # on_delete -- specifing the consequence when the associated user is deleted
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
  first_name = models.CharField(max_length=32,)
  last_name= models.CharField(max_length=32)
  phone = models.CharField(max_length=12)
  age = models.PositiveIntegerField(default=20)

  def __str__(self):
    return f'{self.user.username} Profile'
  
#   # save the image after resizing it
  def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.image.path)

    if (img.height > 200 or img.width > 200):
      output_size = (200, 200)
      img.thumbnail(output_size)
      img.save(self.image.path)

# class Profile1(models.Model):
#   # on_delete -- specifing the consequence when the associated user is deleted
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
#   first_name = models.CharField(max_length=32,)
#   last_name= models.CharField(max_length=32)
#   phone = models.CharField(max_length=12)
#   age = models.PositiveIntegerField(default=20)

#   def __str__(self):
#     return f'{self.user.username} Profile'
  
# #   # save the image after resizing it
#   def save(self, *args, **kwargs):
#     super().save()

#     img = Image.open(self.image.path)

#     if (img.height > 200 or img.width > 200):
#       output_size = (200, 200)
#       img.thumbnail(output_size)
#       img.save(self.image.path)