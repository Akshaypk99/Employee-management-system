from django.db import models

# Create your models here.
from django.conf import settings

class FormTemplate(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField(default=list)

class Employee(models.Model):
    form = models.ForeignKey(FormTemplate, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.JSONField(default=dict)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employees_created")
    created_at = models.DateTimeField(auto_now_add=True)
