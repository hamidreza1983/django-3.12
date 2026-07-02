from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from services.models import *
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import ServicesSerializers
from ...models import Services
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
@permission_classes([IsAdminOrReadOnly])
def services(request):
    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServicesSerializers(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = ServicesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "data created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAdminOrReadOnly])
def service_detail(request, pk):
    service = get_object_or_404(Services, pk=pk)
    if request.method == 'GET':
        serializer = ServicesSerializers(service)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ServicesSerializers(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "data created successfully"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        service.delete()
        return Response({"message" : "data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

