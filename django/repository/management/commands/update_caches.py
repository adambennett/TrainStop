from django.core.management.base import BaseCommand
from django.test.client import RequestFactory
from django.conf import settings

from repository.api.v1.viewsets import PackageViewSet


class Command(BaseCommand):
    help = "Updates repository specific caches"

    def handle(self, *args, **kwargs):
        print("Updating caches")
        request = RequestFactory().get("/api/v1/package/", SERVER_NAME=settings.SERVER_NAME)
        view = PackageViewSet.as_view({"get": "list"})
        PackageViewSet.update_cache(view, request)
        print("Caches updated!")
