from django.test import TestCase
from django.urls import resolve
from tombApp.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "Home resolves incorrectly")

    def testHomePageH1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Welcome to the Tomb of Horrors</h1>', html, 'H1 contents fail')

