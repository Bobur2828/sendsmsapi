
from django.urls import path
from .views import *
urlpatterns = [
    path('send_sms/',SendSMS.as_view(), name='send_sms'),
    path('send_sms_with_token/',SendSMS_with_token.as_view(), name='send_sms'),


]
