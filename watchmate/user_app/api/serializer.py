from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        
        write_only=True,
        style={'input_type':'password'},
        required=True,
        validators=[validate_password],
    )   
    confirm_password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'},
        required=True,
        validators=[validate_password],
    )
    email=serializers.EmailField(required=True)
    
    
    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

    def validate_email(self,email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exist")
        return email
    
    def validate(self,data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("Password does not match")
        return data
    
    def create(self,validate_data):
        validate_data.pop('confirm_password')
        user=User.objects.create(username=validate_data['username'],email=validate_data['email'])
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


