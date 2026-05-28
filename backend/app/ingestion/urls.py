from django.urls import path

from .views import (
    UploadCSVView,
    UploadedCSVListView
)

urlpatterns = [

    path(
        "upload/",
        UploadCSVView.as_view(),
        name="upload_csv"
    ),

    path(
        "all/",
        UploadedCSVListView
        .as_view(),
        name="all_csv"
    ),

]