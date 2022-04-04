# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from email import message
from itertools import product
from pickle import FALSE
from turtle import mode
from django.db import models


class LoanDetails(models.Model):
    state_name = models.CharField(max_length=300, null=True, blank=True)
    client_number = models.CharField(max_length=300, null=True, blank=True)
    loan_account_number = models.CharField(max_length=300, null=True, blank=True)
    branch_name = models.CharField(max_length=300, null=True, blank=True)
    center_id = models.CharField(max_length=300, null=True, blank=True)
    center_name = models.CharField(max_length=300, null=True, blank=True)
    edo_id = models.CharField(max_length=300, null=True, blank=True)
    edo_name = models.CharField(max_length=300, null=True, blank=True)
    product_id = models.CharField(max_length=300, null=True, blank=True)
    client_name = models.CharField(max_length=300, null=True, blank=True)
    co_borrower_name = models.CharField(max_length=300, null=True, blank=True)
    disbursed_loan_amount = models.CharField(max_length=300, null=True, blank=True)
    loan_date = models.CharField(max_length=300, null=True, blank=True)
    repayment_frequency = models.CharField(max_length=300, null=True, blank=True)
    no_of_installments = models.CharField(max_length=300, null=True, blank=True)
    no_of_instalment_remain = models.CharField(max_length=300, null=True, blank=True)
    first_payment_date = models.CharField(max_length=300, null=True, blank=True)
    installment_amount = models.CharField(max_length=300, null=True, blank=True)
    instalment_type = models.CharField(max_length=300, null=True, blank=True)
    interest_rate = models.CharField(max_length=300, null=True, blank=True)
    maturitydate = models.CharField(max_length=300, null=True, blank=True)
    total_principal_due_amount = models.CharField(max_length=300, null=True, blank=True)
    total_interest_due_amount = models.CharField(max_length=300, null=True, blank=True)
    principal_os_amount = models.CharField(max_length=300, null=True, blank=True)
    interest_os_amount = models.CharField(max_length=300, null=True, blank=True)
    insurance = models.CharField(max_length=300, null=True, blank=True)
    loan_cycle = models.CharField(max_length=300, null=True, blank=True)
    total_principal = models.CharField(max_length=300, null=True, blank=True)
    total_interest = models.CharField(max_length=300, null=True, blank=True)

