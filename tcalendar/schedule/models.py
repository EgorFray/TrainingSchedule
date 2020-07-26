from django.db import models
# Create your models here.


class Schedule(models.Model):
   # user = models.ForeignKey(default=1)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    exercise = models.CharField(max_length=50, blank=True)




