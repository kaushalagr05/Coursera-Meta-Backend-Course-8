from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuTest(TestCase):
    """
    Test suite for the Menu model representation.
    """
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    """
    Test suite for the Menu API views.
    """
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=12.50, inventory=40)
        self.item3 = Menu.objects.create(title="Pasta", price=10.00, inventory=35)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
