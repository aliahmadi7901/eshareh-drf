from django.contrib.auth import logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from account.serializers import UserSerializer


class RegisterApiView(APIView):
    def post(self, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "ثبت نام انجام شد."
            data['phone_number'] = account.phone_number
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)


class LogoutApiView(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
