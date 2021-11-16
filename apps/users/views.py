from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.serializers import UserSerializer

from rest_framework import generics
from apps.users.models import Usuario

#Imports para verify Token

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer





# Create your views here.

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.serializers import UserSerializer


class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class UserDetailView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all().values('username','password','documento','email','nombres','apellidos')
    serializer_class = UserSerializer


class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data=request.data)
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        try:
            serializer.is_valid(raise_exception=True)
            token_data = tokenBackend.decode(request.data['token'],verify=False)
            serializer.validated_data['Username'] = token_data['usuario_username']
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)