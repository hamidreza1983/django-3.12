from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from services.models import *
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import ServicesSerializers
from ...models import Services
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin

from rest_framework.viewsets import ModelViewSet





class SerivcesView(ModelViewSet):
    serializer_class = ServicesSerializers
    permission_classes = [AllowAny]
    queryset = Services.objects.filter(status=True)





#class ServicesListView(ListAPIView, ListCreateAPIView):
#    serializer_class = ServicesSerializers
#    permission_classes = [AllowAny]#

#    def get_queryset(self):
#        return Services.objects.all()#

#    def get(self, request, *args, **kwargs):
#        return super().get(request, *args, **kwargs)#

#    def post(self, request, *args, **kwargs):
#        return super().post(request, *args, **kwargs)#

#class ServiceDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):#

#    serializer_class = ServicesSerializers
#    permission_classes = [AllowAny]
#    queryset = Services.objects.filter(status=True)#

#    def get(self, request, *args, **kwargs):
#        return self.retrieve(request, *args, **kwargs)#

#    def put(self, request, *args, **kwargs):
#        return self.update(request, *args, **kwargs)#

#    def delete(self, request, *args, **kwargs):
#        return self.destroy(request, *args, **kwargs)





#class ServiceDetailView(APIView):#

#    def get_permissions(self):
#        if self.request.method == "GET":
#            return ([AllowAny()])
#        return ([IsAdminUser()])
#    
#    def get_object(self, id):
#        service = get_object_or_404(Services, pk=id)
#        return service#

#    def get(self, request, pk):
#        service = self.get_object(pk)
#        serializer = ServicesSerializers(service)
#        return Response(serializer.data, status=status.HTTP_200_OK)#

#    def put(self, request, pk):
#        #service = get_object_or_404(Services, pk=pk)
#        service = self.get_object(pk)
#        serializer = ServicesSerializers(service, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"message" : "data created successfully"}, status=status.HTTP_202_ACCEPTED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    
#    def delete(self, request, pk):
#        #service = get_object_or_404(Services, pk=pk)
#        service = self.get_object(pk)
#        service.delete()
#        return Response({"message" : "data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




#class ServicesListView(GenericAPIView, ListModelMixin, CreateModelMixin):
#    serializer_class = ServicesSerializers
#    permission_classes = [AllowAny]#

#    def get_queryset(self):
#        return Services.objects.all()#

#    def get(self, request,*args, **kwargs):
#        return self.list(request, *args, **kwargs)#

#    def post(self, request,*args, **kwargs):
#        return self.create(request, *args, **kwargs)



#class ServicesListView(GenericAPIView):
#    serializer_class = ServicesSerializers
#    permission_classes = [AllowAny]#
#

#    def get_queryset(self):
#        return Services.objects.all()
#    #

#    def get(self, request, *args, **kwargs):
#        services = self.get_queryset()
#        serializer = self.serializer_class(services, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)#

#    def post(self, request, *args, **kwargs):
#        serializer = self.serializer_class(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({"message" : "data created successfully"}, status=status.HTTP_201_CREATED)




#class ServicesListView(APIView):
#    def get_permissions(self):
#        if self.request.method == "GET":
#            return ([AllowAny()])
#        return ([IsAdminUser()])#

#    def get(self, request, *args, **kwargs):
#        services = Services.objects.all()
#        serializer = ServicesSerializers(services, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)#

#    def post(self, request, *args, **kwargs):
#        serializer = ServicesSerializers(data=request.data)
##        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response({"message" : "data created successfully"}, status=status.HTTP_201_CREATED)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"message" : "data created successfully"}, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#


#@api_view(["GET", "POST"])
#@permission_classes([IsAdminOrReadOnly])
#def services(request):
#    if request.method == 'GET':
#        services = Services.objects.all()
#        serializer = ServicesSerializers(services, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    elif request.method == "POST":
#        serializer = ServicesSerializers(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"message" : "data created successfully"}, status=status.HTTP_201_CREATED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#


#@api_view(["GET", "PUT", "DELETE"])
#@permission_classes([IsAdminOrReadOnly])
#def service_detail(request, pk):
#    service = get_object_or_404(Services, pk=pk)
#    if request.method == 'GET':
#        serializer = ServicesSerializers(service)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    elif request.method == "PUT":
#        serializer = ServicesSerializers(service, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({"message" : "data created successfully"}, status=status.HTTP_202_ACCEPTED)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method == "DELETE":
#        service.delete()
#        return Response({"message" : "data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


