from ninja import ModelSchema
from services.models import Service as ModelService


class Service(ModelSchema):
    class Config:
        model = ModelService
        model_fields = ['id', 'description', 'price']
