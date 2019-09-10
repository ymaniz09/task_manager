from django.db import models

# Create your models here.


class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ("H", "HIGH"),
        ("R", "REGULAR"),
        ("L", "LOW"),
    ]

    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=300, null=False, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, null=False, blank=False)
