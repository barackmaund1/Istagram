from django.urls import path
from . import views
from .views import PostListView,PostCreateView,PostDetailView,UserPostListView,PostUpdateView,PostDeleteView,CreateComment
urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', CreateComment.as_view(), name='comment'),
]