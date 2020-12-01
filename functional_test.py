from selenium import webdriver
import unittest
class FunctionalTest(unittest.TestCase):
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        #self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
    def tearDown(self):
        self.browser.quit()
    
    #@unittest.SkipTest
    def test_title(self):
        self.assertIn('Django', self.browser.title, 'Wrong Title')

if __name__ == '__main__':
    #if calls the class if it is not instantiated elsewhere
    unittest.main()