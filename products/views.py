from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer, ProductListSerializer
from users.permissions import ActiveUserPerms


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    default_serializer = ProductSerializer
    serializers = {
        'list': ProductListSerializer,
        'retrieve': ProductSerializer,
    }
    permission_classes = [ActiveUserPerms]
