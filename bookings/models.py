from django.db import models


class Booking(models.Model):

    STATUS_CHOICES = (
        ("1", "Agendado"),
        ("2", "Atentido"),
        ("3", "Não Atendido"),
        ("4", "Cancelado"),
        ("5", "Faltou"),
        ("6", "Remarcar")
    )

    patient = models.ForeignKey("patients.Patient", on_delete=models.SET_NULL, null=True)
    professional = models.ForeignKey("professionals.Professional", on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey("services.Service", on_delete=models.SET_NULL, null=True)
    date = models.CharField(max_length=50)
    start = models.BigIntegerField(null=False)
    end = models.BigIntegerField(null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
