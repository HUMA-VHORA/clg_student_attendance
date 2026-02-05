from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication


def role_required(allowed_roles):
    """
    allowed_roles = ['Teacher'] or ['Student'] or ['Teacher', 'Admin']
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):

            jwt_auth = JWTAuthentication()

            try:
                # Authenticate JWT
                user, validated_token = jwt_auth.authenticate(request)

                if user is None:
                    return Response(
                        {"error": "Authentication required"},
                        status=status.HTTP_401_UNAUTHORIZED
                    )

                # 🔹 Step 1: Try role from JWT payload
                role = validated_token.get("role")

                # 🔹 Step 2: Fallback → Django Group
                if not role:
                    groups = user.groups.values_list("name", flat=True)
                    role = groups[0] if groups else None

                if not role:
                    return Response(
                        {"error": "Role not assigned"},
                        status=status.HTTP_403_FORBIDDEN
                    )

                if role not in allowed_roles:
                    return Response(
                        {"error": "Access denied for this role"},
                        status=status.HTTP_403_FORBIDDEN
                    )

                # Attach role for later use (optional)
                request.user_role = role

                return view_func(self, request, *args, **kwargs)

            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        return wrapper
    return decorator
