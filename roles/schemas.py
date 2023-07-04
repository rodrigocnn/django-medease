from ninja import ModelSchema
from roles.models import Role as ModelRole


class Role(ModelSchema):
    class Config:
        model = ModelRole
        model_fields = ['id', 'description']
