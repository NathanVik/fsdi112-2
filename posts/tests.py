from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase, TestCase
from .models import Post
from django.urls import reverse


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="A test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}" # f strings to format the string
        self.assertEqual(expected_object_name, "A test")

    
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Another Test")

    def test_homepage_uses_correct_model(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Another Test")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "post_list.html")
    
    def test_view_extends_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")

class DetailViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="third test")

    def test_detail_url_exists_at_location(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)
    
    def test_detail_url_by_name(self):
        response = self.client.get(reverse("post_detail", args=[1]))
        self.assertEqual(response.status_code, 200)
    
    def test_detail_uses_correct_template(self):
        response = self.client.get(reverse("post_detail", args=[1]))
        self.assertTemplateUsed(response, "post_detail.html")
    
    def test_detail_extends_correct_template(self):
        response = self.client.get(reverse("post_detail", args=[1]))
        self.assertTemplateUsed(response, "base.html")