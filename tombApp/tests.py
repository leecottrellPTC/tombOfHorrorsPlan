from django.test import TestCase
from django.urls import resolve
from tombApp.views import home_page
from tombApp.views import lore_page
from django.http import HttpRequest
import unittest


# Create your tests here.
class HomePageTest(TestCase):
    
    @unittest.skip('just because')
    def testHomePage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page, "Home resolves incorrectly")

    def testHomePageH1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Welcome to the Tomb of Horrors</h1>', html, 'H1 contents fail')

    def testLorePage(self):
        request = HttpRequest()
        response = lore_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<p>Self-resetting traps were built into the plan, traps so deadly that they could snuff the life from even the most experienced adventurer at once. Enchanted creatures, not many, were left in key places.</p>', html, 'Lore Paragraph contents fail')

    def testMenuLinks(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('href="lore.html"', html, 'Link to lore.html not found')
        self.assertIn('href="home.html"', html, 'Link to home.html not found')
        
    def testImageOnHome(self):
        request = HttpRequest()
        response = lore_page(request)
        html = response.content.decode('utf8')
        self.assertIn('src="images/acererak.jpg"', html, 'Acererak image code not on page')
        

