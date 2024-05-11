from django.db import models


class Clients(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    passport = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return (f'[ name:{self.first_name} {self.last_name}, '
                f'email:{self.email}, '
                f'passport:{self.passport} ]')


class InsuranceObject(models.Model):
    object_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return (f'[ name:{self.object_name}, '
                f'description:{self.description} ]')


class Contracts(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    object_id = models.ForeignKey(InsuranceObject, on_delete=models.CASCADE)
    contract_date = models.CharField(max_length=100)
    insurance_payment = models.FloatField()

    def __str__(self):
        return (f'[ client_id:{self.client_id}, '
                f'object_id:{self.object_id}, '
                f'contract_date:{self.contract_date}, '
                f'insurance_payment:{self.insurance_payment} ]')


class InsurancePayments(models.Model):
    contract_id = models.ForeignKey(Contracts, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

    def __str__(self):
        return (f'[ concept_id:{self.contract_id}, '
                f'date:{self.date} ]')
