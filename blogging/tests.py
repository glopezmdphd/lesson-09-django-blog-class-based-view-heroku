import datetime
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category


class PostTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""

    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.now = timezone.now()
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count, text="foo", author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()
        # Print all posts to verify they are created
        for post in Post.objects.all():
            print(post.title, post.published_date)

    def test_list_only_published(self):
        resp = self.client.get("/blogging/")
        resp_text = resp.content.decode(resp.charset)
        print(resp_text)  # Add this line to print the response content
        self.assertTrue("My Cool Blog Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)
