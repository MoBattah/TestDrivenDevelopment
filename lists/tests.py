from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_to_do_lists(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn("to-do item", response.content.decode())

    def test_home_page_can_remember_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        self.assertIn('A new item', response.content.decode())