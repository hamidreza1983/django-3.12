from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import RegistrationSerializer
from ...models import UserModel
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import LoginTokenSerializer

class SignupApiView(GenericAPIView):
    permission_classes = [(AllowAny)]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "detail" : "user created suucessfully"
        }
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    serializer_class = LoginTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, create = Token.objects.get_or_create(user=user)
        return Response ({
            "detail" : "login successfully",
            "email" : user.email,
            "token" : token.key
        },
        status=status.HTTP_202_ACCEPTED
        )
