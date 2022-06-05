from rest_framework import serializers
from .models import Msg
from django.contrib.auth.models import User


class MsgSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Msg
        fields = ('creator','receiver', 'subject', 'message', 'creation_date', 'unread')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    msgs = serializers.PrimaryKeyRelatedField(many=True, queryset=Msg.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'msgs')
