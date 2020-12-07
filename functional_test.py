from selenium import webdriver
import unittest
class FunctionalTest(unittest.TestCase):
    
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        #simply choose the desired head option
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        #self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
    #def tearDown(self):
    #    self.browser.quit()
    
    #@unittest.SkipTest
    def test_title(self):
        self.assertIn('Tomb of Horrors', self.browser.title, 'Wrong Title')

    def testLink(self):
        self.browser.get('http://localhost:8000')
        loreLink = self.browser.find_element_by_partial_link_text("Lore").click()
        self.assertIn('Lore', self.browser.title, 'Lore Link did not take to correct page')
        
    def testCharCreate(self):
        self.browser.get('http://localhost:8000/character.html')
        self.browser.find_element_by_id("charname").sendkeys("Kaladin")
        self.browser.find_element_by_id("hitpoints").sendkeys("60")
        self.browser.find_element_by_id("armor").sendkeys("15")


        

if __name__ == '__main__':
    #if calls the class if it is not instantiated elsewhere
    unittest.main()