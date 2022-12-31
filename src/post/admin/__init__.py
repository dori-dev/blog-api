from django.contrib import admin

from post.admin.post import PostAdmin
from post.models import (
    Post as PostModel,
)

admin.site.register(PostModel, PostAdmin)
