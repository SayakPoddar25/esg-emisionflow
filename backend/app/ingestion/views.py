from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)

from .serializers import UploadedCSVSerializer
from .models import UploadedCSV

from .parsers import parse_csv
from .normalizers import normalize_row

from app.emmision.models import (
    EmissionRecord
)


class UploadCSVView(APIView):

    parser_classes = (
        MultiPartParser,
        FormParser
    )

    def get(self, request):

        return Response({
            "message":
            "Upload endpoint working"
        })

    def post(self, request):

        serializer = UploadedCSVSerializer(
            data=request.data
        )

        if serializer.is_valid():

            uploaded = serializer.save()

            rows = parse_csv(
                uploaded.file.path
            )

            for row in rows:

                normalized = normalize_row(row)

                EmissionRecord.objects.create(

                    source=normalized["source"],

                    date=normalized["date"],

                    unit=normalized["unit"],

                    value=normalized["value"],

                    original_source=
                    uploaded.category
                )

            uploaded.is_processed = True
            uploaded.save()

            return Response(
                {
                    "message":
                    "Upload success"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UploadedCSVListView(
    APIView
):

    def get(self, request):

        files = (
            UploadedCSV.objects
            .all()
            .order_by("-uploaded_at")
        )

        serializer = UploadedCSVSerializer(
            files,
            many=True
        )

        return Response(
            serializer.data
        )