from netbox.filtersets import NetBoxModelFilterSet
from .models import SiteDocument, DeviceDocument, CircuitDocument
from django.db.models import Q

class SiteDocumentFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = SiteDocument
        fields = ('id', 'name', 'document_type', 'site')

    def search(self, queryset, name, value):
        return (
            queryset.filter(
                Q(name__icontains=value) | Q(document__icontains=value)
            )
            if value.strip()
            else queryset
        )

class DeviceDocumentFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = DeviceDocument
        fields = ('id', 'name', 'document_type', 'device')

    def search(self, queryset, name, value):
        return (
            queryset.filter(
                Q(name__icontains=value) | Q(document__icontains=value)
            )
            if value.strip()
            else queryset
        )

class CircuitDocumentFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = CircuitDocument
        fields = ('id', 'name', 'document_type', 'circuit')

    def search(self, queryset, name, value):
        return (
            queryset.filter(
                Q(name__icontains=value) | Q(document__icontains=value)
            )
            if value.strip()
            else queryset
        )
