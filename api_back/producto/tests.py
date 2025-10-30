from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto
import uuid


class ProductoAPITests(APITestCase):

    def setUp(self):
        # Crear un producto inicial para probar la lista
        self.producto = Producto.objects.create(
            nombre="Producto Test",
            descripcion="Descripción del producto test",
            precio=99.99
        )
        self.url = reverse('product-list-create')

    def test_list_productos(self):
        """
        Verifica que la vista GET '/productos/' devuelva los productos existentes
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debe haber un producto
        self.assertEqual(response.data[0]['nombre'], "Producto Test")

    def test_create_producto(self):
        """
        Verifica que la vista POST '/productos/' cree un nuevo producto
        """
        data = {
            "nombre": "Nuevo Producto",
            "descripcion": "Descripción del nuevo producto",
            "precio": "123.45"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 2)  # Ahora hay 2 productos
        self.assertEqual(Producto.objects.last().nombre, "Nuevo Producto")