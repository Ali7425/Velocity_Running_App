from django.shortcuts import render

from rest_framework import generics
from .models import Run
from .serializers import RunSerializer

# This view will handle listing all runs and creating a new run.
class RunListCreateView(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    