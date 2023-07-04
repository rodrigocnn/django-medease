from typing import Optional
from ninja import ModelSchema
from professionals.models import Professional


class ProfessionalSchema(ModelSchema):

    role_description: Optional[str] = None

    class Config:
        model = Professional
        model_exclude = ['created_at', 'updated_at']
