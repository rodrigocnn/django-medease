from django.shortcuts import get_object_or_404
from ninja import Router
from services.models import Service as ServiceModel
from services.schemas import Service
from typing import List

router = Router()


@router.get('', response=List[Service])
def index(request):
    roles = ServiceModel.objects.all()
    return roles


@router.post("", response={201: Service})
def store(request, payload: Service):
    role = ServiceModel.objects.create(**payload.dict())
    return role


@router.get("/show/{role_id}", response={200: Service})
def show(request, role_id: int):
    role = get_object_or_404(ServiceModel, id=role_id)
    return 200, role


@router.put("/{role_id}",  response={200: Service})
def update(request, role_id: int, payload: Service):
    role = get_object_or_404(ServiceModel, id=role_id)
    role.description = payload.description
    role.save()
    return 200, role


@router.delete("/{role_id}", response={204: None})
def delete(request, role_id: int):
    role = get_object_or_404(ServiceModel, id=role_id)
    role.delete()
    return 204, {"success": True}
