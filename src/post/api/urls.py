from django.urls import path
from post.api import views

app_name = 'post'
urlpatterns = [
    path(
        'all/',
        views.PostList.as_view(),
        name='post_list',
    ),
    path(
        '<int:pk>/',
        views.PostDetail.as_view(),
        name='post_detail',
    ),
]
