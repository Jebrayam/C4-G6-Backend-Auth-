# REST
from rest_framework import serializers
# Local
from c4_mercar_auth import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["id", "email", "name", "last_name", "password"]
