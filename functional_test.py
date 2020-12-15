from selenium import webdriver
import unittest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FunctionalTest(unittest.TestCase):
    
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless=True
        #simply choose the desired head option
        self.browser = webdriver.Firefox(options=fireFoxOptions)
        #self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
    def tearDown(self):
        self.browser.quit()
    
    @unittest.SkipTest
    def test_title(self):
        self.assertIn('Tomb of Horrors', self.browser.title, 'Wrong Title')
    
    @unittest.SkipTest
    def testLink(self):
        self.browser.get('http://localhost:8000')
        loreLink = self.browser.find_element_by_partial_link_text("Lore").click()
        self.assertIn('Lore', self.browser.title, 'Lore Link did not take to correct page')
    
    @unittest.SkipTest   
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

    @unittest.SkipTest
    def testImageLoads(self): 
        resp = requests.head('http://localhost:8000/static/images/tombMouth.jpg')
        self.assertEqual(200, resp.status_code, 'tombmouth.jpg does not load')

    @unittest.SkipTest
    def testCSSFileExists(self): 
        resp = requests.head('http://localhost:8000/static/darkly.css')
        self.assertEqual(200, resp.status_code, 'darkly.css load')

    
    def testMinotaur(self):
        self.browser.get('http://localhost:8000/tobattle.html')
        critterName = self.browser.find_element_by_id("critterName")
        critterHP = self.browser.find_element_by_id("critterHP")
        critterImg = self.browser.find_element_by_id("critterImg")
        critterAC = self.browser.find_element_by_id("critterAC")
        critterDam = self.browser.find_element_by_id("critterDam")

        self.assertEqual("76", critterHP.text,"Critter HP is incorrect")
        self.assertEqual("Minotaur", critterName.text,"Critter Name is incorrect")
        self.assertEqual("14", critterAC.text,"Critter AC is incorrect")
        self.assertEqual("17", critterDam.text,"Critter Damage is incorrect")
        self.assertIn("minotaur.png", critterImg.get_attribute("src"),"Critter Image is incorrect")

    def testToBattle(self):
        self.browser.get('http://localhost:8000/character.html')
        self.browser.find_element_by_id("charname").send_keys("Kaladin")
        self.browser.find_element_by_id("hitpoints").send_keys("60")
        self.browser.find_element_by_id("armor").send_keys("15")
        self.browser.find_element_by_id("submit").click()      
        
        self.browser.find_element_by_id("battleBtn").click()

        charname = self.browser.find_element_by_id("charname")
        self.assertIn("Kaladin", charname.text, "Character name is incorrect")
        hp = self.browser.find_element_by_id("hp")
        self.assertEqual("60", hp.text,"HP is incorrect")
        ac = self.browser.find_element_by_id("ac")
        self.assertEqual("15", ac.text,"AC is incorrect")




        

if __name__ == '__main__':
    #if calls the class if it is not instantiated elsewhere
    unittest.main()