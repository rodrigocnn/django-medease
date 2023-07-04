from django.shortcuts import get_object_or_404
from ninja import Router
from roles.models import Role as RoleModel
from roles.schemas import Role
from typing import List

router = Router()


@router.get('', response=List[Role])
def index(request):
    roles = RoleModel.objects.all()
    return roles


@router.post("", response={201: Role})
def store(request, payload: Role):
    role = RoleModel.objects.create(**payload.dict())
    return role


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
