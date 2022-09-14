from rest_framework import routers
from rest_framework_nested import routers
from django.urls import path, include
from EpicEventsAPI.views import (
    # ProjectViewSet,
    # IssueViewSet,
    # CommentViewSet,
    # ContributorViewSet,
)


router = routers.DefaultRouter()
# router.register(r"projects", ProjectViewSet)

# projects_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
# projects_router.register(r"issues", IssueViewSet, basename="issues")
# projects_router.register(r"users", ContributorViewSet, basename="users")

# issues_router = routers.NestedSimpleRouter(projects_router, r"issues", lookup="issue")
# issues_router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path(r"", include(router.urls)),
    # path(r"", include(projects_router.urls)),
    # path(r"", include(issues_router.urls)),
]