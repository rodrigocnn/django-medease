from ninja import ModelSchema
from patients.models import Patient as PatientModel


class Patient(ModelSchema):
    class Config:
        model = PatientModel
        model_exclude = ['created_at', 'updated_at']
