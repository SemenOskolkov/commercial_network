from django.core.management import BaseCommand


from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            {
                'name': 'МФУ лазерное Pantum',
                'model': 'M6507',
                'release_date': '2021-02-16'
            },
            {
                'name': 'МФУ лазерное Pantum',
                'model': 'M6500W',
                'release_date': '2021-08-27'
            },
            {
                'name': '3D принтер Wanhao Duplicator',
                'model': 'D12/300',
                'release_date': '2022-04-18'
            },
            {
                'name': '3D принтер Wanhao',
                'model': 'GR2',
                'release_date': '2022-07-02'
            },
            {
                'name': 'ПК Atlas',
                'model': 'H332',
                'release_date': '2023-02-08'
            },
        ]

        products_list = []
        Product.objects.all().delete()

        for item in products:
            products_list.append(Product(**item))

        Product.objects.bulk_create(products_list)
