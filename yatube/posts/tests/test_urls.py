from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from posts.models import Group, Post

User = get_user_model()


class GrropURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='',
            slug='',
            description=''

        )
        cls.post = Post.objects.create(
            text='',
            author='',
            group=''
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='neo')
        self.author = User.objects.create_user(username='auth')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.authorized_client.force_login(self.author)

    def test_urls_correct_template(self):
        templates_url_name = {
            'posts/index.html': '/',
            'posts/group_list': '/group/<slug>/',
            'posts/profile': '/profile/<username>/',
            'posts/posts_detail': '/post/<post_id>/',
        }
        for template, address in templates_url_name.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address
                                                      )
                self.assertTemplateUsed(response, template)
