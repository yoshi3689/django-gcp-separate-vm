from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # we have to tell django to redirect to the page below after being created
    def get_absolute_url(self):
        # return reverse("post-detail", kwargs={"pk": self.pk})
        return reverse("blog-home")
        # reverse -- just returns the url string
        # redirect -- actually redirect to the give url
    