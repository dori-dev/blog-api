from django.contrib import admin

from posts.admin.post import PostAdmin
from posts.models import (
    Post as PostModel,
)

admin.site.register(PostModel, PostAdmin)
