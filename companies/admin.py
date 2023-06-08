from django.urls import reverse
from django.contrib import admin

from companies.models import Company


# @admin.action(description="Clear the debt to the supplier")
# def clear_debt(modeladmin, request, queryset):
#     queryset.update(dept=0.00)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'type_company', 'email', 'country', 'city', 'street', 'house_number', 'products', 'provider_link',
        'dept', 'time_of_creation',)
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, queryset):
        queryset.update(dept=0.00)

    clear_debt.short_description = "Clear the debt to the supplier"


    def provider_link(self, obj):
        if obj.provider:
            return u'<a href="{0}">{1}</a>'.format(
                reverse('admin:companies_company_changelist', args=(obj.provider.pk,)), obj.provider)

    provider_link.allow_tags = True
    provider_link.admin_order_field = 'provider'
    provider_link.short_description = Company._meta.get_field('provider').verbose_name.title()
