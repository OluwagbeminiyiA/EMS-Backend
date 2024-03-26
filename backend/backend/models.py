import django.utils.timezone
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=200, default="Female")
    marital_status = models.CharField(max_length=200, default="Single")
    date_joined = models.DateTimeField(default=django.utils.timezone.now())
    highest_education = models.CharField(max_length=500, default="College")
    skills = models.TextField(default="Python")
    manager = models.CharField(max_length=500, default="Gbeminiyi A.")
    basic_salary = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    hra_allowance = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    additional_allowance = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    professional_tax = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    medical_premium = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    income_tax = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    pf_deductions = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    gross_earning = models.DecimalField(max_digits=200, decimal_places=3, default=0)
    gross_deduction = models.DecimalField(max_digits=200, decimal_places=3, default=0)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_id = models.CharField(max_length=200)
    project_name = models.CharField(max_length=500)
    project_domain = models.CharField(max_length=500)
    client_name = models.CharField(max_length=300)
    project_description = models.TextField(default='')
    required_resources = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    project_manager = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=django.utils.timezone.now())
    end_date = models.DateTimeField(default=django.utils.timezone.now())

    def __str__(self):
        return self.project_name
