from django.db import models


class ReviewLog(models.Model):

    ACTION_CHOICES = [
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    emission_id = models.IntegerField()

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    reviewed_at = models.DateTimeField(
        auto_now_add=True
    )

    reviewer_note = models.TextField(
        blank=True
    )

    def __str__(self):

        return (
            f"{self.emission_id}"
            f" - "
            f"{self.action}"
        )