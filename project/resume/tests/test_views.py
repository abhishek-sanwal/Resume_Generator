from django.test import TestCase, Client
from django.urls import reverse
from ..models import Profile

from django.http import HttpResponse
from unittest.mock import patch


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.p1 = Profile.objects.create(
            name='test1',
            email="a@gmail.com",
            phone="1234567890",
            summary="test summary",
            degree="test degree",
            school="test school",
            university="test university",
            previous_work="test previous work",
            skills="test skills"
        )
        self.p2 = Profile.objects.create(
            name='test2',
            email="a@gmail.com",
            phone="1234567890",
            summary="test summary",
            degree="test degree",
            school="test school",
            university="test university",
            previous_work="test previous work",
            skills="test skills"
        )

        self.p3 = Profile.objects.create(
            name='test3',
            email="a@gmail.com",
            phone="1234567890",
            summary="test summary",
            degree="test degree",
            school="test school",
            university="test university",
            previous_work="test previous work",
            skills="test skills"
        )

    def test_accept_GET(self):
        response = self.client.get(reverse('accept'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accept.html')

    def test_accept_POST(self):
        response = self.client.post(reverse('accept'), {
            'name': 'test4',
            'email': 'test@gmail.com',
            'phone': '1234567890',
            'summary': 'test summary',
            'degree': 'test degree',
            'school': 'test school',
            'university': 'test university',
            'previous_work': 'test previous work',
            'skills': 'test skills'
        })

        response2 = self.client.post(reverse('accept'), {
            'email': 'test@gmail.com',
            'phone': '1234567890',
            'summary': 'test summary',
            'degree': 'test degree',
            'school': 'test school',
            'university': 'test university',
            'previous_work': 'test previous work',
            'skills': 'test skills'
        })

        response3 = self.client.post(reverse('accept'), {
            'name': 'test4',
            'phone': '1234567890',
            'summary': 'test summary',
            'degree': 'test degree',
            'school': 'test school',
            'university': 'test university',
            'previous_work': 'test previous work',
            'skills': 'test skills'
        })

        response4 = self.client.post(reverse('accept'), {
            'name': 'test4',
            'email': 'test@gmail.com',
            'summary': 'test summary',
            'degree': 'test degree',
            'school': 'test school',
            'university': 'test university',
            'previous_work': 'test previous work',
            'skills': 'test skills'
        })

        self.assertEquals(response2.status_code, 400)
        self.assertEquals(response3.status_code, 400)
        self.assertEquals(response4.status_code, 400)
        self.assertIn('error', response2.context)
        self.assertIn('error', response3.context)
        self.assertIn('error', response4.context)
        self.assertEqual(
            response2.context['error'], 'Please fill all the fields')
        self.assertEqual(
            response3.context['error'], 'Please fill all the fields')
        self.assertEqual(
            response4.context['error'], 'Please fill all the fields')
        self.assertEquals(response.status_code, 200)
        profile = Profile.objects.get(name='test4')
        self.assertNotEqual(profile, None)
        self.assertEqual(profile.name, 'test4')

    def test_list_GET(self):
        response: HttpResponse = self.client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)
        # data = response.json()
        self.assertEqual(len(response.context["profiles"]), 3)
        self.assertEqual(response.context["profiles"][0], self.p1)
        self.assertEqual(response.context["profiles"][1], self.p2)
        self.assertEqual(response.context["profiles"][2], self.p3)
        self.assertTemplateUsed(response, 'list.html')

    def test_resume_GET(self):
        response = self.client.get(reverse('resume', args=[self.p1.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume.html')
        self.assertEqual(response.context["user_profile"], self.p1)
        self.assertEqual(response.headers['Content-Disposition'], 'attachment')
        self.assertEqual(response.headers['Content-Type'], 'application/pdf')
        self.assertTemplateUsed(response, 'resume.html')
        # template = loader.get_template('resume.html')
        # print(template.options)

    # @patch('builtins.__import__')
    # def test_import_error_with_mock(self, mock_import):
    #     # Mock the import to raise ImportError
    #     mock_import.side_effect = ImportError("Couldn't import Django. Are you sure it's installed and "
    #                                           "available on your PYTHONPATH environment variable? Did you "
    #                                           "forget to activate a virtual environment?")

    #     # Test that ImportError is raised when trying to import a non-existent module
    #     with self.assertRaises(ImportError) as context:
    #         safe_import('non_existent_module')

    #     # Verify that the raised exception message is correct
    #     self.assertIn("Couldn't import Django. Are you sure it's installed and "
    #                   "available on your PYTHONPATH environment variable? Did you "
    #                   "forget to activate a virtual environment?", str(context.exception))

    def tearDown(self):
        Profile.objects.all().delete()
        return super().tearDown()
