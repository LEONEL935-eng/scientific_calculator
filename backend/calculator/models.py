from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"
from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"
# calculator/models.py

from django.db import models

class Operation(models.Model):
    input1 = models.FloatField()
    input2 = models.FloatField()
    result = models.FloatField()
    operation_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.input1} {self.operation_type} {self.input2} = {self.result}"

