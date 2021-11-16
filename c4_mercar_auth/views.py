from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import generics
from c4_mercar_auth import models
from c4_mercar_auth import serializers

from c4_mercar_auth import models, serializers

class UserProfileCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserProfileSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        tokenData = {
            "email" : request.data["email"],
            "password" : request.data["password"]
        }

        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)

        return Response(
            tokenSerializer.validated_data,
            status = status.HTTP_201_CREATED
        )

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset         = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
