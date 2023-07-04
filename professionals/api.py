from django.shortcuts import get_object_or_404
from ninja import Router
from professionals.models import Professional
from professionals.schemas import ProfessionalSchema
from typing import List

from roles.models import Role

router = Router()


@router.get('', response=List[ProfessionalSchema])
def index(request):
    professionals = Professional.objects.all()
    professional_data = []
    for professional in professionals:
        professional_data.append({
            'id': professional.id,
            'name': professional.name,
            'role_description': professional.role.description,
            'email': professional.email,
            'date_of_birth': professional.date_of_birth,
            'phone': professional.phone,
            'rg': professional.rg,
            'cpf': professional.cpf,
            'address': professional.address,
            'district': professional.district,
            'city': professional.city,
            'state': professional.state,

        })
    return professional_data


@router.post("", response={201: ProfessionalSchema})
def store(request, payload: ProfessionalSchema):
    role = Role.objects.get(pk=payload.role)
    professional = Professional.objects.create(
            name=payload.name,
            email=payload.email,
            role=role,
            date_of_birth=payload.date_of_birth,
            phone=payload.phone,
            rg=payload.rg,
            cpf=payload.cpf,
            address=payload.address,
            district=payload.district,
            city=payload.city,
            state=payload.state
        )

    professional.save()
    return 201, professional


@router.get("/show/{professional_id}", response={200: ProfessionalSchema})
def show(request, professional_id: int):
    professional = get_object_or_404(Professional, id=professional_id)
    professional.role_description = professional.role.description
    return 200, professional


@router.put("/{professional_id}",  response={200: ProfessionalSchema})
def update(request, professional_id: int, payload: ProfessionalSchema):
    professional = get_object_or_404(Professional, id=professional_id)
    role = Role.objects.get(pk=payload.role)
    professional.name = payload.name
    professional.role = role
    professional.date_of_birth = payload.date_of_birth
    professional.phone = payload.phone
    professional.rg = payload.rg
    professional.cpf = payload.cpf
    professional.address = payload.address
    professional.district = payload.district
    professional.city = payload.city
    professional.state = payload.state
    professional.save()
    return 200,  professional


@router.delete("/{professional_id}", response={204: None})
def delete(request, professional_id: int):
    professional = get_object_or_404(Professional, id=professional_id)
    professional.delete()
    return 204, {"success": True}
