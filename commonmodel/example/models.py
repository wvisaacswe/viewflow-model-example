from django.db import models
from viewflow.models import Process


class Department(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
         return self.label

class CheckRequestProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

class TimeOffRequestProcess(Process):
    reason = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )