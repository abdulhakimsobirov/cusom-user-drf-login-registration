from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from django.contrib.auth.password_validation import password_changed
from django.contrib.auth import authenticate, login

from rest_framework import status
from config.mixins import ListAPIViewResponseMixin, RetrieveAPIViewResponseMixin
from config.responses import ResponseSuccess, ResponseFail
from .models import User
from .serializer import RegistrationSerializer, LoginSerializer, ChangePasswordSerializer, UserEditSerialzier, UserSerializer



def get_token_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }