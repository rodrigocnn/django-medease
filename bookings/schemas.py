from typing import Optional
from ninja import ModelSchema
from bookings.models import Booking


class BookingSchema(ModelSchema):

    professional_name: Optional[str] = None
    patient_name: Optional[str] = None
    service_name: Optional[str] = None
    professional: Optional[int] = None
    service: Optional[int] = None
    patient: Optional[int] = None

    class Config:
        model = Booking
        model_exclude = ['created_at', 'updated_at']


class BookingSchemaStore(ModelSchema):

    class Config:
        model = Booking
        model_exclude = ['created_at', 'updated_at']
