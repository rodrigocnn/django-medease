
from django.http import HttpRequest
from ninja.security import HttpBasicAuth
from django.conf import settings
from django.contrib.auth.models import User
import jwt


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request: HttpRequest):
        authorization_header = request.META.get('HTTP_AUTHORIZATION', '')
        if authorization_header.startswith('Bearer'):
            token = authorization_header.split(' ')[1]
            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token.get('user_id')
                if user_id:
                    user = User.objects.get(id=user_id)
                    return user
            except jwt.DecodeError:
                return None
            except User.DoesNotExist:
                return None
