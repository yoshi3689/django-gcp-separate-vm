from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    # class based view needs this extraction
    path('', PostListView.as_view(), name='blog-home'),
    # query parameter in django
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]