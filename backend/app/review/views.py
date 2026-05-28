from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.emmision.models import (
    EmissionRecord
)

from .models import (
    ReviewLog
)

from .serializers import (
    ReviewLogSerializer
)


class ReviewListView(APIView):

    def get(self, request):

        emissions = (
            EmissionRecord
            .objects
            .all()
            .order_by(
                "-uploaded_at"
            )
        )

        data = []

        for item in emissions:

            data.append({

                "id":
                item.id,

                "source":
                item.source,

                "value":
                item.value,

                "unit":
                item.unit,

                "date":
                item.date,

                "status":
                item.status,

                "original_source":
                item.original_source
            })

        return Response(data)


class ApproveRejectView(
    APIView
):

    def post(
        self,
        request,
        emission_id
    ):

        action = request.data.get(
            "action"
        )

        try:

            emission = (
                EmissionRecord
                .objects.get(
                    id=emission_id
                )
            )

        except EmissionRecord.DoesNotExist:

            return Response(
                {
                    "error":
                    "Emission not found"
                },
                status=
                status.HTTP_404_NOT_FOUND
            )

        if action not in [
            "approved",
            "rejected"
        ]:

            return Response(
                {
                    "error":
                    "Invalid action"
                },
                status=
                status.HTTP_400_BAD_REQUEST
            )

        emission.status = action
        emission.save()

        ReviewLog.objects.create(
            emission_id=
            emission.id,

            action=
            action,

            reviewer_note=
            request.data.get(
                "note",
                ""
            )
        )

        return Response(
            {
                "message":
                f"{action} success"
            }
        )
class DashboardStatsView(
    APIView
):

    def get(
        self,
        request
    ):

        fuel_count = (
            EmissionRecord
            .objects
            .filter(
                source="sap"
            )
            .count()
        )

        utility_count = (
            EmissionRecord
            .objects
            .filter(
                source="utility"
            )
            .count()
        )

        travel_count = (
            EmissionRecord
            .objects
            .filter(
                source="travel"
            )
            .count()
        )

        pending_count = (
            EmissionRecord
            .objects
            .filter(
                status="pending"
            )
            .count()
        )

        approved_count = (
            EmissionRecord
            .objects
            .filter(
                status="approved"
            )
            .count()
        )

        rejected_count = (
            EmissionRecord
            .objects
            .filter(
                status="rejected"
            )
            .count()
        )

        return Response({

            "fuel":
            fuel_count,

            "utility":
            utility_count,

            "travel":
            travel_count,

            "pending":
            pending_count,

            "approved":
            approved_count,

            "rejected":
            rejected_count
        })