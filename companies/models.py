from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Company(models.Model):
    FACTORY = 'factory'
    RETAIL_NETWORK = 'retail_network'
    INDIVIDUAL_ENTREPRENEUR = 'individual_entrepreneur'

    TYPE = (
        ('factory', 'завод;'),
        ('retail_network', 'розничная сеть'),
        ('individual_entrepreneur', 'индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='Название')
    type_company = models.CharField(max_length=50, choices=TYPE, verbose_name='Тип компании')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    products = models.ForeignKey('products.Product', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    dept = models.DecimalField(max_digits=21, decimal_places=2, verbose_name='Задолженность')
    time_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'

    def __str__(self):
        return f'{self.name} {self.type_company} {self.time_of_creation}'
