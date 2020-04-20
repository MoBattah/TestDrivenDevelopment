from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_to_do_lists(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn("to-do item", response.content.decode())

    def test_home_page_can_save_post_requests_to_database(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'
        response = home_page(request)

        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')

        self.assertIn('A new item', response.content.decode())



from lists.models import Item

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items_to_the_database(self):

        # Testing creation and saving of two new items

        first_item = Item()
        first_item.text = "Item the first"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, "Item the first")

        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, "Item the second")


