from rest_framework import serializers

from apps.user.models import User
import re


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'email', 'date_joined', 'phone_number')
        
    def validate_phone_number(self, value):
        # Проверка номера телефона
        if not re.match(r'^\(\+996\)\d{9}$', value):
            raise serializers.ValidationError("Неверный формат номера телефона!")
        return value
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'password', 'confirm_password', 'phone_number')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs 
  
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # class UserNumberSerializer(serializers.ModelSerializer):
    #  class Meta:
    #     model = User
    #     fields = '__all__'

    # def validate_phone_number(self, value):
    #     # Проверка номера телефона
    #     if not re.match(r'^\(\+996\)\d{9}$', value):
    #         raise serializers.ValidationError("Неверный формат номера телефона!")
    #     return value