from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Schedule(models.Model):
    month = models.IntegerField(
        default=1,
        unique=False,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1),
    ])
    day = models.IntegerField(
        default=1,
        unique=False,
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1),
        ]
    )
    time = models.TimeField(null=True, blank=True)
    exercise = models.CharField(max_length=50, blank=True)
