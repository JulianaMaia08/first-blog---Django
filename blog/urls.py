from django.urls import path
from .views import PostList, PostDetail, NewPost, ThanksPostView

app_name = "blog"

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/new', NewPost.as_view(), name='post_new'),
    path('post/thanks_post/', ThanksPostView.as_view(), name='thanks_post'),
]