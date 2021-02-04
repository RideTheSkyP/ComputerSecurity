from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class TransferFieldSerializer(serializers.ModelSerializer):
    transferFrom = serializers.IntegerField()
    transferTo = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = models.Transfers
        fields = ('transferFrom', 'transferTo', 'amount')

    def create(self, validated_data):
        print("Val data: ", validated_data)
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        # if password is not None:
        #     instance.set_password(password)
        # instance.save()
        # return instance