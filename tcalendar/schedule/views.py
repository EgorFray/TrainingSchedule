from django.shortcuts import render
from rest_framework import viewsets
from .models import Schedule
from .serializers import ScheduleSerialier
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ScheduleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleSerialier(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Schedule.objects.create()
        serializer = ScheduleSerialier(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerialier(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerialier(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
