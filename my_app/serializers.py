from rest_framework import serializers
from rest_framework.validators import ValidationError

class SendMessageSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=12)

    def validate_phone_number(self, value):
        try:
            int(value)  
        except ValueError:
            raise ValidationError("Telefon raqami faqat sonlardan iborat emas")

        if len(value) != 9:
            raise ValidationError("Telefon raqamini +998 larsiz kiriting ")
        
        return value

    message = serializers.CharField(max_length=255)


class SendMessageSerializer1(serializers.Serializer):
    email =serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=9)
    def validate_phone_number(self, value):
        try:
            int(value)  
        except ValueError:
            raise ValidationError("Telefon raqami faqat sonlardan iborat emas")

        if len(value) != 9:
            raise ValidationError("Telefon raqamini +998 larsiz kiriting ")
        
        return value
    message = serializers.CharField(max_length=255)