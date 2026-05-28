from django.contrib import admin

from .models import (
    UploadedCSV
)


@admin.register(
    UploadedCSV
)
class UploadedCSVAdmin(
    admin.ModelAdmin
):

    list_display = (
        "id",
        "category",
        "original_filename",
        "uploaded_at",
        "is_processed",
    )

    search_fields = (
        "category",
        "original_filename",
    )

    list_filter = (
        "category",
        "is_processed",
    )