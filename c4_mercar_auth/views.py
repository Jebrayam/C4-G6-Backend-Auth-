from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import generics
from c4_mercar_auth import models
from c4_mercar_auth import serializers

from django.conf                          import settings
from rest_framework                       import status
from rest_framework_simplejwt.views       import TokenVerifyView
from rest_framework_simplejwt.backends    import TokenBackend
from rest_framework_simplejwt.exceptions  import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer

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

class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data = request.data)
        tokenBackend = TokenBackend(algorithm = settings.SIMPLE_JWT["ALGORITHM"])

        try:
            serializer.is_valid(raise_exception = True)
            token_data = tokenBackend.decode(
                request.data["token"],
                verify = False
            )
            serializer.validated_data["UserId"] = token_data["user_id"]
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(
            serializer.validated_data,
            status = status.HTTP_200_OK
        )
