
from rest_framework import viewsets
from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.response import Response
from rest_framework import status



class ScheduleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, user):
        queryset = Schedule.objects.create()
        serializer = ScheduleSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, user, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Schedule.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
