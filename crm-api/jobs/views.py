from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer
from rest_framework import viewsets

# GET     /api/jobs/
# POST    /api/jobs/
# GET     /api/jobs/<id>/
# PUT     /api/jobs/<id>/
# DELETE  /api/jobs/<id>/


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
