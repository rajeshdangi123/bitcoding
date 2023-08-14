from django.db import models


class Bom(models.Model):
    part_number = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.part_number


class Disti(models.Model):
    part_number = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.part_number


class Unified(models.Model):
    bom_pn = models.CharField(max_length=100, blank=True, null=True)
    bom_qty = models.IntegerField(null=True)
    disti_pn = models.CharField(max_length=100, blank=True, null=True)
    disti_qty = models.IntegerField(blank=True, null=True)
    error_flag = models.CharField(max_length=100)
