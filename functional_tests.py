import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        
        #Edith goes to the homepage
        self.browser.get('http://localhost:8000')

        #Edith sees the browser title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)
        
        
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #She types "Buy peacock feathers" into the inputbox
        inputbox.send_keys("Buy peacock feathers")
        

if __name__ == '__main__':
    unittest.main()