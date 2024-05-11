from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    print(request.user.id)
    client = get_object_or_404(Clients, pk=request.user.id)
    return render(request, "insurance/index.html", {"client": client})


def login(request):
    pass


def signup(request):
    pass


def clients_cabinet(request, id):
    client = get_object_or_404(Clients, pk=id)
    contracts = Contracts.objects.filter(client_id=id)
    return render(request, "insurance/cabinet.html",
                  {"client": client, "contracts": contracts,
                   "series": client.passport[:4], "number": client.passport[4:10]})


def contract_detail(request, id):
    client = get_object_or_404(Clients, pk=id)
    contracts = Contracts.objects.filter(client_id=id)
    detail = []
    for contract in contracts:
        detail.append(
            contract
        )
    print(f"detail {detail}")
    return render(request, "insurance/contract_details.html",
                  {"client": client, "details": detail})


def order_insurance(request, id):
    client = get_object_or_404(Clients, pk=id)

    pass

