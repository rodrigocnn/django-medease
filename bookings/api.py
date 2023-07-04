from django.shortcuts import get_object_or_404
from ninja import Router
from bookings.models import Booking
from bookings.schemas import BookingSchema, BookingSchemaStore
from typing import Any, List
from patients.models import Patient

from professionals.models import Professional
from services.models import Service


router = Router()


@router.get('', response=List[BookingSchema])
def index(request):
    bookings = Booking.objects.all()
    bookings_data = []

    for booking in bookings:
        bookings_data.append({
            'id': booking.id,
            'professional_name': booking.professional.name,
            'professional':  booking.professional.id,
            'service': booking.service.id,
            'service_name': booking.service.description,
            'patient': booking.patient.id,
            'patient_name': booking.patient.name,
            'date': booking.date,
            'start': booking.start,
            'end': booking.end,
            'status': booking.status

        })
    return bookings_data


@router.post("", response={201: BookingSchemaStore})
def store(request, payload: BookingSchemaStore):

    professional = Professional.objects.get(pk=payload.professional)
    patient = Patient.objects.get(pk=payload.patient)
    service = Service.objects.get(pk=payload.service)

    booking = Booking.objects.create(
            date=payload.date,
            start=payload.start,
            end=payload.end,
            status=payload.status,
            professional=professional,
            patient=patient,
            service=service,

        )
    booking.save()
    return 201, booking


@router.get("/show/{booking_id}", response={200: Any})
def show(request, booking_id: int):
    booking = get_object_or_404(Booking, id=booking_id)
    booking_data = {
        'id': booking.id,
        'professional_name': booking.professional.name,
        'professional': booking.professional.id,
        'service': booking.service.id,
        'service_name': booking.service.description,
        'patient': booking.patient.id,
        'patient_name': booking.patient.name,
        'date': booking.date,
        'start': booking.start,
        'end': booking.end,
        'status': booking.status

        }
    return 200, booking_data


@router.put("/{booking_id}",  response={200: BookingSchemaStore})
def update(request, booking_id: int, payload: BookingSchema):

    professional = Professional.objects.get(pk=payload.professional)
    patient = Patient.objects.get(pk=payload.patient)
    service = Service.objects.get(pk=payload.service)
    booking = get_object_or_404(Booking, id=booking_id)
    booking.date = payload.date
    booking.start = payload.start
    booking.end = payload.end
    booking.status = payload.status
    booking.professional = professional
    booking.patient = patient
    booking.service = service
    booking.save()
    return 200,  booking


@router.delete("/{booking_id}", response={204: None})
def delete(request, booking_id: int):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return 204, {"success": True}
