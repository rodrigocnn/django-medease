from django.shortcuts import get_object_or_404
from ninja import Router
from patients.models import Patient as PatientModel
from patients.schemas import Patient
from typing import List


router = Router()


@router.get('', response=List[Patient])
def index(request):
    patients = PatientModel.objects.all()
    return patients


@router.post("", response={201: Patient})
def store(request, payload: Patient):
    patient = PatientModel.objects.create(**payload.dict())
    patient.save()
    return 201, patient


@router.get("/show/{patient_id}", response={200: Patient})
def show(request, patient_id: int):
    patient = get_object_or_404(PatientModel, id=patient_id)
    return 200, patient


@router.put("/{patient_id}",  response={200: Patient})
def update(request, patient_id: int, payload: Patient):
    patient = get_object_or_404(PatientModel, id=patient_id)
    patient.name = payload.name
    patient.email = payload.email
    patient.date_of_birth = payload.date_of_birth
    patient.phone = payload.phone
    patient.rg = payload.rg
    patient.cpf = payload.cpf
    patient.address = payload.address
    patient.district = payload.district
    patient.city = payload.city
    patient.state = payload.state
    patient.save()
    return 200,  patient


@router.delete("/{patient_id}", response={204: None})
def delete(request, patient_id: int):
    patient = get_object_or_404(PatientModel, id=patient_id)
    patient.delete()
    return 204, {"success": True}
