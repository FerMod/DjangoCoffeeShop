from django.test import TestCase
from django.urls import reverse

from products.models import Product

# Create your tests here.
class ProductListViewTests(TestCase):

    def test_returns_200(self):
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 0)

    def test_returns_200_with_product(self):
        url = reverse('product_list')
        Product.objects.create(
            name='test',
            description='test description',
            price=2.8,
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)
