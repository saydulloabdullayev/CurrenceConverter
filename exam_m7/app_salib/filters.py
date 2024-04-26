from rest_framework.filters import BaseFilterBackend
import coreapi

class SalibFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name='keyword',
                location='query',
                required=False,
                type='str',
                description='Search keyword'
            )
        ]
        return fields

    def filter_queryset(self, request, queryset, view):
        return  queryset