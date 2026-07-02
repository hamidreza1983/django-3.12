from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from services.api.v1.serializers import ServicesSerializers, CategorySerializers
from rest_framework import status
from services.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly




@api_view()
def last_services(request):
    last_three_services = Services.objects.filter(status=True).order_by('-created_at')[:3]
    serializer = ServicesSerializers(last_three_services, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAdminUser])
def categories(request):
    cats = Category.objects.all()
    serializer = CategorySerializers(cats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)