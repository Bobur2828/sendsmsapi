from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SendMessageSerializer,SendMessageSerializer1
from .send_sms import SendSms,SendSms_with
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class SendSMS(GenericAPIView):
    serializer_class = SendMessageSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data.get('message')
            phone = serializer.validated_data.get('phone_number')
            e_api = SendSms(message=message, phone=phone)
            r=e_api.send()  
            data={
                "status": r,

                "message": message,
                "phone_number": phone
            }
            return Response(data)
        else:
            return Response(serializer.errors)


class SendSMS_with_token(GenericAPIView):
    serializer_class = SendMessageSerializer1

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            message = serializer.validated_data.get('message')
            phone = serializer.validated_data.get('phone_number')
            e_api = SendSms_with(message=message, phone=phone, email=email, password=password)
            r = e_api.send()  
            data = {
                "status": r,
                "message": message,
                "phone_number": phone,
                "email": email,
                "password": password
                
            }
            return Response(data)
        else:
            return Response(serializer.errors)

