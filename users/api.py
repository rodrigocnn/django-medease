from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from typing import List
from ninja import Router
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from roles.models import Role as RoleModel
from roles.schemas import Role
from users.schemas import UserSchema, UserSchemaAuth, UserSchemaStore

router = Router()


@router.post("/auth", auth=None, response={201: UserSchema})
def login(request, payload: UserSchemaAuth):
    user = auth.authenticate(username=payload.username, password=payload.password)

    if user:
        # Generate JWT token
        token_payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)  # Token expiration time
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({'token': token}, status=201)
    else:
        return JsonResponse({'detail': 'Invalid credentials'}, status=401)


@router.get('', response=List[Role])
def index(request):
    roles = RoleModel.objects.all()
    return roles


@router.post("", response={201: UserSchema})
def store(request, payload: UserSchemaStore):

    if User.objects.filter(email=payload.email).exists():
        return 409, {"this email already exists!!": True}

    username = payload.email
    email = payload.email
    password = payload.password
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return 201, {
        "email": user.email,
        "username": user.username,
    }


@router.get("/show/{role_id}", response={200: Role})
def show(request, role_id: int):
    role = get_object_or_404(RoleModel, id=role_id)
    return 200, role


@router.put("/{role_id}",  response={200: Role})
def update(request, role_id: int, payload: Role):
    role = get_object_or_404(RoleModel, id=role_id)
    role.description = payload.description
    role.save()
    return 200, role


@router.delete("/{role_id}", response={204: None})
def delete(request, role_id: int):
    role = get_object_or_404(RoleModel, id=role_id)
    role.delete()
    return 204, {"success": True}
