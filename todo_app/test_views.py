from django.test import TestCase
from .models import Item

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/todo_list.html')

        
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name="Test Todo Item")

        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_app/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name':'Test Addded Item'})
        self.assertRedirects(response, "/")


    def test_can_edit_item(self):
        item = Item.objects.create(name="Test Todo Item")

        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, '/')
        existing_item = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_item),0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name="Test Todo Item", done=True)

        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, '/')
        upated_item = Item.objects.get(id=item.id)
        
        self.assertTrue(upated_item.done)



