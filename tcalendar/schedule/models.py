from django.db import models
from django.conf import settings


class Schedule(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    exercise = models.CharField(max_length=50, blank=True)




