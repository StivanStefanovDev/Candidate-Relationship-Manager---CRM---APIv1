from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobViewSet

# GET     /api/jobs/
# POST    /api/jobs/
# GET     /api/jobs/<id>/
# PUT     /api/jobs/<id>/
# DELETE  /api/jobs/<id>/

router = DefaultRouter()
router.register(r"jobs", JobViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
