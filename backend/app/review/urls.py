from django.urls import path

from .views import (

    ReviewListView,
    ApproveRejectView,
    DashboardStatsView
)

urlpatterns = [

    path(
        "",
        ReviewListView.as_view(),
        name="review_list"
    ),

    path(
        "stats/",
        DashboardStatsView.as_view(),
        name="dashboard_stats"
    ),

    path(
        "<int:emission_id>/",
        ApproveRejectView.as_view(),
        name="approve_reject"
    ),
]