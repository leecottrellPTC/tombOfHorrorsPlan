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
    
    @unittest.SkipTest
    def test_title(self):
        self.assertIn('Tomb of Horrors', self.browser.title, 'Wrong Title')
    
    @unittest.SkipTest
    def testLink(self):
        self.browser.get('http://localhost:8000')
        loreLink = self.browser.find_element_by_partial_link_text("Lore").click()
        self.assertIn('Lore', self.browser.title, 'Lore Link did not take to correct page')
        
    def testCharCreate(self):
        self.browser.get('http://localhost:8000/character.html')
        self.browser.find_element_by_id("charname").send_keys("Kaladin")
        self.browser.find_element_by_id("hitpoints").send_keys("60")
        self.browser.find_element_by_id("armor").send_keys("15")
        self.browser.find_element_by_id("submit").click()

        self.assertIn('Kaladin', self.browser.title, 'Name not in title')
        hp = self.browser.find_element_by_id("hp")
        self.assertEqual("60", hp.text,"HP is incorrect")
        ac = self.browser.find_element_by_id("ac")
        self.assertEqual("15", ac.text,"AC is incorrect")
        



        

if __name__ == '__main__':
    #if calls the class if it is not instantiated elsewhere
    unittest.main()