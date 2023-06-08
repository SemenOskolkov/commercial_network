from rest_framework.routers import DefaultRouter

from companies.apps import CompaniesConfig
from companies.views import CompanyViewSet

app_name = CompaniesConfig.name

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = []

urlpatterns += router.urls
