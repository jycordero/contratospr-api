from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from .views import (
    ContractorViewSet,
    ContractViewSet,
    DocumentViewSet,
    EntityViewSet,
    ServiceGroupViewSet,
    ServiceViewSet,
)

router = DefaultRouter()
router.register(r"contracts", ContractViewSet)
router.register(r"documents", DocumentViewSet)
router.register(r"contractors", ContractorViewSet)
router.register(r"entities", EntityViewSet)
router.register(r"service-groups", ServiceGroupViewSet)
router.register(r"services", ServiceViewSet)

urlpatterns = [
    path("v1/", include((router.urls, "api"), namespace="v1")),
    path("v1/docs/", include_docs_urls(title="Contratos de Puerto Rico")),
]
