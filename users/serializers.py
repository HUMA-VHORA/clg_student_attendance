from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Adds user role into JWT payload
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Extract role from Django Group
        groups = user.groups.values_list('name', flat=True)
        token['role'] = groups[0] if groups else None

        return token
