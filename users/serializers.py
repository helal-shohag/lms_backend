from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password

class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','username','email','role','mobile_no','created_at','updated_at','password']

def create(self,validated_data):
    validated_data['password'] =make_password(validated_data['password'])        
    return super().create(validated_data)