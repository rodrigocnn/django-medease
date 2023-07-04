from django.db import models


class Professional(models.Model):
    name = models.CharField(max_length=50, unique=True)
    role = models.ForeignKey("roles.Role", on_delete=models.SET_NULL, null=True, related_name='role')
    email = models.CharField(max_length=80, unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=50)
    rg = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


