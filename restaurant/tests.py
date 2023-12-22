from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80.22, inventory=100)
        itemstr=item.get_item()
        self.assertEqual(itemstr, "IceCream : 80.22")