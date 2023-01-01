from django.urls import path
from post.api.views import post

app_name = 'post'
urlpatterns = [
    path(
        'all/',
        post.PostList.as_view(),
        name='post_list',
    ),
    path(
        '<int:pk>/',
        post.PostDetail.as_view(),
        name='post_detail',
    ),
]
