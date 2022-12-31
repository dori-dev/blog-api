from django.test import TestCase
from django.contrib.auth.models import User as UserModel
from django.contrib.auth import get_user_model
from posts.models import Post

User: UserModel = get_user_model()


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        user_1 = User.objects.create_user(
            username='test',
            password='1234',
        )
        user_1.save()
        # Create a blog post
        post_1 = Post.objects.create(
            author=user_1,
            title='The Sample Blog Title',
            body='This is the sample body content',
        )
        post_1.save()

    def test_blog_content(self):
        post = Post.objects.first()
        author: UserModel = post.author
        title = post.title
        body = post.body
        self.assertEqual(author.username, 'test')
        self.assertEqual(title, 'The Sample Blog Title')
        self.assertNotEqual(title, 'The sample blog title')
        self.assertEqual(body, 'This is the sample body content')
        self.assertNotEqual(body, 'this is the sample body content')
