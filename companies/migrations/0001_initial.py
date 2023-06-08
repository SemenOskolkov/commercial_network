# Generated by Django 3.0 on 2023-06-08 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('type_company', models.CharField(choices=[('factory', 'завод;'), ('retail_network', 'розничная сеть'), ('individual_entrepreneur', 'индивидуальный предприниматель')], max_length=50, verbose_name='Тип компании')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
                ('dept', models.DecimalField(decimal_places=2, max_digits=21, verbose_name='Задолженность')),
                ('time_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product', verbose_name='Продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.Company', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
    ]
