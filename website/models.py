from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    ident_id = models.CharField(max_length=14, null=False, blank=False)
    contribution_time = models.IntegerField(default=0, null=False, blank=False)
    remuneration = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    objects = models.Manager()
    