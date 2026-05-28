from django.contrib import admin

from .models import (
    EmissionRecord
)


@admin.register(
    EmissionRecord
)
class EmissionRecordAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "source",
        "value",
        "unit",
        "status",
    )

    search_fields = (
        "source",
    )

    list_filter = (
        "status",
        "unit",
    )