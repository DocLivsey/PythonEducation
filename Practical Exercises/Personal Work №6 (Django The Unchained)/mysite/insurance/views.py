from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *


def index(request):
    print(f"auth: {request.user.is_authenticated}, id = {request.user.id}")
    if request.user.is_authenticated:
        client = get_object_or_404(Clients, pk=request.user.id)
        return render(request, "insurance/index.html",
                      {"client": client, "show_cabinet": True, "logged_in": True,
                       "define_passport": client.passport != 'undefined'})
    else:
        return render(request, "insurance/index.html",
                      {"show_cabinet": False, "logged_in": False})


def log_out(request):
    logout(request)
    return render(request, "insurance/index.html",
                  {"show_cabinet": False, "logged_in": False})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('<h1>Authenticated successfully</h1>'
                                        "<a href='../'>Home Page</a> / "
                                        f"<a href='../../insurance/{user.id}/'>Personal Cabinet</a>")
                else:
                    return HttpResponse('<h1>Disabled account</h1>')
            else:
                return HttpResponse('<h1>Invalid login</h1>')
    else:
        form = LoginForm()
    return render(request, 'insurance/login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                return HttpResponse("<h1>You are already registered</h1>"
                                    "<a href=''>Home Page</a>")
            else:
                login(request, user)
                client = Clients(first_name=form.cleaned_data.get('first_name'),
                                 last_name=form.cleaned_data.get('last_name'),
                                 email=form.cleaned_data.get('email'),
                                 passport='undefined')
                client.save()
                return redirect("")
    else:
        form = SignUpForm()
    return render(request, "insurance/signup.html", {'form': form})


def clients_cabinet(request, id):
    client = get_object_or_404(Clients, pk=id)
    contracts = Contracts.objects.filter(client_id=id)
    return render(request, "insurance/cabinet.html",
                  {"client": client, "contracts": contracts,
                   "series": client.passport[:4], "number": client.passport[4:10],
                   "define_passport": client.passport != 'undefined'})


def contract_detail(request, id):
    client = get_object_or_404(Clients, pk=id)
    contracts = Contracts.objects.filter(client_id=id)
    detail = []
    for contract in contracts:
        detail.append(
            contract
        )
    return render(request, "insurance/contract_details.html",
                  {"client": client, "details": detail})


def order_insurance(request, id):
    context = {}
    client = get_object_or_404(Clients, pk=id)
    if request.method == 'POST':
        form = OrderInsuranceForm(request.POST)
        if form.is_valid():
            object_name = form.cleaned_data.get('object_name')
            description = form.cleaned_data.get('description')
            contract_date = form.cleaned_data.get('contract_date')
            insurance_payment = form.cleaned_data.get('insurance_payment')
            insurance_object = InsuranceObject(object_name=object_name, description=description)
            insurance_object.save()
            contract = Contracts(contract_date=contract_date, insurance_payment=insurance_payment,
                                 client_id_id=id, object_id_id=insurance_object.id)
            contract.save()
            context = {'form': form, 'client': client, 'contract': contract, "object": insurance_object}
            return render(request, "insurance/cabinet.html",
                          {"client": client, "contracts": Contracts.objects.filter(client_id=id),
                           "series": client.passport[:4], "number": client.passport[4:10],
                           "define_passport": client.passport != 'undefined'})
    else:
        form = OrderInsuranceForm()
        context = {'form': form, 'client': client}
    return render(request, "insurance/make_order.html", context)


def change_personal_data(request, id):
    client = get_object_or_404(Clients, pk=id)
    if request.method == 'POST':
        form = ChangePersonalDataForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('first_name'):
                client.first_name = form.cleaned_data.get('first_name')
            if form.cleaned_data.get('last_name'):
                client.last_name = form.cleaned_data.get('last_name')
            if form.cleaned_data.get('email'):
                client.email = form.cleaned_data.get('email')
            if form.cleaned_data.get('passport'):
                client.passport = form.cleaned_data.get('passport')
            client.save()
            return render(request, "insurance/cabinet.html",
                          {"client": client, "contracts": Contracts.objects.filter(client_id=id),
                           "series": client.passport[:4], "number": client.passport[4:10],
                           "define_passport": client.passport != 'undefined'})
    else:
        form = ChangePersonalDataForm()
        return render(request, "insurance/change_personal_data.html",
                      {"client": client, 'form': form})
