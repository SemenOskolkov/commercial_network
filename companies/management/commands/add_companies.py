from django.core.management import BaseCommand

from companies.models import Company
from products.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        companies = [
            {
                'name': 'GLOBALPrintTech',
                'type_company': Company.FACTORY,
                'email': 'gpt@site.com',
                'country': 'Россия',
                'city': 'Москва',
                'street': 'Промышленный',
                'house_number': '43а',
                'products': [
                    Product.objects.filter(pk=1).first(),
                    Product.objects.filter(pk=2).first(),
                ],
                'provider': None,
                'dept': 0.00,
            },
            {
                'name': 'HUALIAN 3D Machinery',
                'type_company': Company.FACTORY,
                'email': 'hualian@site.com',
                'country': 'China',
                'city': 'Wenzhou',
                'street': 'Industrial Pack',
                'house_number': '2',
                'products': [
                    Product.objects.filter(pk=3).first(),
                    Product.objects.filter(pk=4).first(),
                ],
                'provider': None,
                'dept': 0.00,
            },
            {
                'name': 'VM Group',
                'type_company': Company.FACTORY,
                'email': 'vmg@site.com',
                'country': 'Россия',
                'city': 'Санкт-Петербург',
                'street': 'Приморская',
                'house_number': '45/3',
                'products': [
                    Product.objects.filter(pk=5).first(),
                    Product.objects.filter(pk=2).first(),
                ],
                'provider': Company.objects.filter(pk=1).first(),
                'dept': 543000.00,
            },
            {
                'name': 'ТехноМир',
                'type_company': Company.RETAIL_NETWORK,
                'email': 'techworld@site.ru',
                'country': 'Россия',
                'city': 'Москва',
                'street': 'Ленина',
                'house_number': '84',
                'products': [
                    Product.objects.filter(pk=1).first(),
                ],
                'provider': Company.objects.filter(pk=1).first(),
                'dept': 543000.00,
            },
            {
                'name': '3D Технологии',
                'type_company': Company.RETAIL_NETWORK,
                'email': '3dtech@site.ru',
                'country': 'Россия',
                'city': 'Новосибирск',
                'street': 'Луначарского',
                'house_number': '183',
                'products': [
                    Product.objects.filter(pk=4).first(),
                ],
                'provider': Company.objects.filter(pk=2).first(),
                'dept': 1135000.00,
            },
            {
                'name': 'ИП Иванов',
                'type_company': Company.INDIVIDUAL_ENTREPRENEUR,
                'email': 'ivanov@site.ru',
                'country': 'Россия',
                'city': 'Санкт-Петербург',
                'street': 'Восстания',
                'house_number': '32б',
                'products': [
                    Product.objects.filter(pk=4).first(),
                ],
                'provider': Company.objects.filter(pk=5).first(),
                'dept': 200000.00,
            },
            {
                'name': 'ИП Петров',
                'type_company': Company.INDIVIDUAL_ENTREPRENEUR,
                'email': 'petrov@site.ru',
                'country': 'Россия',
                'city': 'Москва',
                'street': 'Пионеров',
                'house_number': '8/2',
                'products': [
                    Product.objects.filter(pk=2).first(),
                ],
                'provider': Company.objects.filter(pk=1).first(),
                'dept': 0.00,
            },
        ]

        Company.objects.all().delete()

        for item in companies:
            companies_item = Company.objects.create(name=item['name'], type_company=item['type_company'],
                                                    email=item['email'], country=item['country'], city=item['city'],
                                                    street=item['street'], house_number=item['house_number'],
                                                    dept=item['dept'])

            # for products_item in item['products']:
            #     companies_item.products.add(products_item)
            #
            # for provider_item in item['provider']:
            #     companies_item.provider.add(provider_item)

            companies_item.save()
