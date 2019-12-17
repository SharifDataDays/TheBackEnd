from django.contrib.auth.models import User
from rest_framework import serializers
from apps.translation.serializer import TranslatedTextSerializer
from apps.translation.models import TranslatedText
from apps.accounts.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = TranslatedTextSerializer()
    last_name = TranslatedTextSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'email', 'birth_date', 'residence', 'education']

    def create(self, validated_data):
        first_name_data = validated_data.pop('first_name')
        last_name_data = validated_data.pop('last_name')
        validated_data['first_name'] = TranslatedText.objects.create( **first_name_data)
        validated_data['last_name'] = TranslatedText.objects.create( **last_name_data)
        return UserProfile.objects.create(**validated_data)
        

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        profile_data['user'] = user.pk
        ser = ProfileSerializer(data=profile_data)
        if ser.is_valid():
            ser.save()
        return user
