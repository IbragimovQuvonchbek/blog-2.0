from .views import PostListView, FullPostView, CreatePostView, UpdatePostView,DeletePostView
from django.urls import path

urlpatterns = [
    path('post/new',CreatePostView.as_view(), name='create_post' ),
    path('',PostListView.as_view(), name='post'),
    path('<int:pk>/', FullPostView.as_view(), name='full_post'),
    path('<int:pk>/edit', UpdatePostView.as_view(), name='edit_post'),
    path('<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]