
from django.test import SimpleTestCase

from django.urls import resolve, reverse
from resume import views


class TestUrls(SimpleTestCase):

    def test_accept_url_resolved(self):

        url = reverse("accept")

        self.assertEqual(resolve(url).func, views.accept,
                         "Accept Url is resolved?")

    def test_list_url_resolve(self):

        url = reverse("list")

        self.assertEqual(resolve(url).func, views.list,
                         "List url is resolved?")

    def test_resume_url_resolve(self):

        url = reverse("resume", args=[2])

        self.assertEqual(resolve(url).func, views.resume,
                         "Resume url is resolved?")
