from django.db import models


class UploadedCSV(models.Model):

    CATEGORY_CHOICES = [
        ("sap", "SAP"),
        ("utility", "UTILITY"),
        ("travel", "TRAVEL"),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    file = models.FileField(
        upload_to="uploads/"
    )

    original_filename = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    source_of_truth = models.CharField(
        max_length=100,
        default="manual_upload"
    )

    is_processed = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):

        if self.file:
            self.original_filename = (
                self.file.name
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f"{self.category}"
            f" - "
            f"{self.original_filename}"
        )