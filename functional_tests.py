import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_starting_a_new_todo_list(self):
        #Edith goes to the homepage
        self.browser.get('http://localhost:8000')

        #Edith sees the browser title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Start a new to-do list', header.text)
        
        
        
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #She types "Buy peacock feathers" into the inputbox
        inputbox.send_keys("Buy peacock feathers")

        # When Edith hits enter, the page updates and now the page lists
        # '1: Buy peacock feathers as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows]
        )

        # Edith wonders whethers the site will remember her list.
        # Then she sees the site has generated a unique URL for her.
        # There is some explanatory text to that effect.

        print("Hello")
        self.fail('Finish the test.')

    def tearDown(self):
        self.browser.quit()



if __name__ == '__main__':
    unittest.main()