from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_to_do_lists(self):
        request = HttpRequest()

        response = home_page(request)
        
        with open('lists/templates/home.html') as f:
            expected_content = f.read()

        self.assertEqual(response.content.decode(), expected_content)
