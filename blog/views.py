from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView
)
from .models import Post

# function-based views
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    # this will let django know which model to use
    model = Post
    # specifies the template to load up
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    # specifies which context object to load on
    context_object_name = 'posts'
    # specifies the order of objects to be displayed based on the value of the attribute
    # newest to oldest -date_posted
    # oldest to newest date_posted-
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'

# this is how you login-required with a class-based view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # assign an author's name to the invisible field
    def form_valid(self, form):
        form.instance.author = self.request.user
        # calling this method on the super[CreateView]
        # with the user name field filled out
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class-based views