from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    organization = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


# Для хакатона
#
#
# class CostCapitalConstraction(models.Model): #Стоимость капитального строительства
#     min = models.IntegerField(max_length=100)
#     max = models.IntegerField(max_length=100)
#
#
# class Accounting(models.Model): #Бухгалтерский учет
#     name = models.CharField(max_length=100)
#     min_osn = models.IntegerField(max_length=10)
#     max_osn = models.IntegerField(max_length=10)
#     min_usn = models.IntegerField(max_length=10)
#     max_usn = models.IntegerField(max_length=10)
#     min_patent = models.IntegerField(max_length=10)
#     max_patent = models.IntegerField(max_length=10)
#
#
# class StateDuty(models.Model): #Госпошлина
#     name = models.CharField(max_length=100)
#     cost = models.IntegerField(max_length=10)
#
#
# class Industry(models.Model): #Обезличенные данные
#     main_branch = models.CharField(max_length=1000)
#     sub_branch = models.CharField(max_length=1000)
#     average_number_staff = models.DecimalField(max_length=100)
#     average_salary = models.DecimalField(max_length=100)
#     taxes_to_budget = models.DecimalField(max_length=100)
#     income_tax = models.DecimalField(max_length=100)
#     property_tax = models.DecimalField(max_length=100)
#     land_tax = models.DecimalField(max_length=100)
#     ndfl = models.DecimalField(max_length=100)
#     transport_tax = models.DecimalField(max_length=100)
#     other_taxes = models.DecimalField(max_length=100)
#
#
# class Machines(models.Model): #Станки средняя цена
#     equipment_type = models.CharField(max_length=100)
#     average_cost_dol = models.DecimalField(max_length=100)
#     avegare_price_rub = models.DecimalField(max_length=100)
#
#
# class CadastravalValue(models.Model): #Средняя кадастровая стоимость
#     district = models.CharField(max_length=100)
#     cost = models.DecimalField(max_length=100)


