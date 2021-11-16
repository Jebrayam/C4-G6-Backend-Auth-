# REST
from rest_framework import serializers
# Local
from c4_mercar_auth import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "password"
        ]
