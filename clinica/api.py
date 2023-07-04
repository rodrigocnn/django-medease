import jwt
from django.contrib import auth
from ninja import NinjaAPI
from ninja.security import HttpBearer
from django.conf import settings
from roles.api import router as roles_router
from services.api import router as services_router
from patients.api import router as patients_router
from professionals.api import router as professionals_router
from bookings.api import router as bookings_router
from users.api import router as users_router


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')
            if user_id:
                user = auth.get_user_model().objects.get(id=user_id)
                return user
        except jwt.DecodeError:
            return None
        except auth.get_user_model().DoesNotExist:
            return None


api = NinjaAPI(auth=AuthBearer())
api.add_router('/users', users_router)
api.add_router("/roles", roles_router)
api.add_router("/services", services_router)
api.add_router("/patients", patients_router)
api.add_router("/professionals", professionals_router)
api.add_router("/bookings", bookings_router)
