from rest_framework.views import APIView
from rest_framework.response import Response

from .models import EmissionRecord
from .serializers import (
    EmissionRecordSerializer
)


class EmissionListView(APIView):

    def get(self, request):

        emissions = (
            EmissionRecord.objects.all()
        )

        serializer = (
            EmissionRecordSerializer(
                emissions,
                many=True
            )
        )

        return Response(serializer.data)