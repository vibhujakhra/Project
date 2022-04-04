# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from telnetlib import STATUS

from django.conf import settings
from rest_framework.response import Response
from .models import *
import re, os
import csv
import pandas as pd
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import DetailView
from .models import LoanDetails


class SheetUploadView(DetailView):

    template_name = 'upload_sheet.html'

    def post(self, request, *args, **kwargs):

        context = dict()
        format = request.POST.get('format')
        try:
            if format == 'csv':
                excel_file = pd.read_csv(
                    request.FILES["excel_file"],
                    keep_default_na=False
                ).fillna(0.0)
            else:
                excel_file = pd.read_excel(
                    request.FILES["excel_file"],
                    engine='openpyxl',
                    keep_default_na=False
                ).fillna(0.0)
        except Exception:
            messages.warning(
                request, 'Kindly provide file in csv or xlsx format only!')
            return render(
                request, 'upload_sheet.html',
                {"context": context}
            )

        destination = open(settings.STATICFILES_DIRS[0]+'/files/tempfile.csv', 'wb+')
        for chunk in request.FILES["excel_file"].chunks():
            destination.write(chunk)
        destination.close()

        # sheet headers
        context['headers'] = excel_file.keys()
        # sheet values
        context['tail'] = excel_file.values
        context['valid_msg'] = 'records uploaded successfully'

        return render(
            request, 'upload_sheet.html',
            {"context": context})


class StoreData(DetailView):

    def post(self, request):
        checked_headers = request.get('checked_headers')
        def parse_row(row):
            STATIC_DICT = {
                "State Name":'state_name',
                "Client Number":'client_number',
                "Loan Account Number":'loan_account_number',
                "Branch Name":'branch_name',
                "Center ID":'center_id',
                "Center Name":'center_name',
                "EDO ID":'edo_id',
                "EDO Name":'edo_name',
                "Product Id":'product_id',
                "Client Name":'client_name',
                "Co Borrower Name":'co_borrower_name',
                "Disbursed Loan Amount":'disbursed_loan_amount',
                "Loan Date":'loan_date',
                "Repayment Frequency":'repayment_frequency',
                "No of Installments":'no_of_installments',
                "No of Instalment remain":'no_of_instalment_remain',
                "First Payment Date":'first_payment_date',
                "Installment Amount":'installment_amount',
                "Instalment Type":'instalment_type',
                "Interest Rate":'interest_rate',
                "MaturityDate":'maturitydate',
                "Total Principal Due Amount":'total_principal_due_amount',
                "Total Interest Due Amount":'total_interest_due_amount',
                "Principal OS Amount":'principal_os_amount',
                "Interest OS Amount":'interest_os_amount',
                "Insurance":'insurance',
                "Loan Cycle":'loan_cycle',
                "Total Principal":'total_principal',
                "Total Interest":'total_interest',
                    }

            temp = {}
            for r in row:
                if r in checked_headers:
                    temp.update({STATIC_DICT.get(r.strip()): row[r]})
            return temp

        try:
            with open(settings.STATICFILES_DIRS[0]+'/files/tempfile.csv', 'rb') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    LoanDetails(**parse_row(row)).save()
            os.delete(settings.STATICFILES_DIRS[0]+'/files/tempfile.csv')
        except Exception:
            messages.warning(
                request, 'File was not accessable!')
            return Response(status=400)
        return Response(status=200)
