from rest_framework import serializers as ser



class RegisterCustomerSerializer(ser.Serializer):
    email = ser.EmailField()
    username = ser.CharField()
    password = ser.CharField()