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
    def to_representation(self, instance):
        UserProfileData = models.UserProfile.objects.get(id = instance.id)
        return {
            "id"          : UserProfileData.id,
            "email"       : UserProfileData.email,
            "first_name"  : UserProfileData.first_name,
            "last_name"   : UserProfileData.last_name,
            "address"     : UserProfileData.address,
            "phone_number": UserProfileData.phone_number
        }
