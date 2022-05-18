from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
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

class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin,):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object
        return self.request.user == post.author

class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin,):
    model = Post
    fields = ['title', 'content']
    # success_url = f'/post/{}'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, DeleteView,UserPassesTestMixin,):
    model = Post
    # needs a destination after deletion since the page itself won;t exist anymore
    success_url = '/'

    def test_func(self):
        post = self.get_object
        return self.request.user == post.author

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class-based views