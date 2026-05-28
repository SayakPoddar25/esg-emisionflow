from django.db import models


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    source = models.CharField(
        max_length=100
    )

    date = models.DateField()

    unit = models.CharField(
        max_length=50
    )

    value = models.FloatField()

    original_source = models.CharField(
        max_length=100,
        default="unknown"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    is_edited = models.BooleanField(
        default=False
    )

    def __str__(self):

        return (
            f"{self.source}"
            f" - "
            f"{self.value}"
        )