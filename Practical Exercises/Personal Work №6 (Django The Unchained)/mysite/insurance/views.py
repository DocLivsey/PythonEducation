from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *


def index(request):
    if request.user.is_authenticated:
        client = get_object_or_404(Clients, pk=request.user.id)
        return render(request, "insurance/index.html", {"client": client, "show_cabinet": True})
    else:
        return render(request, "insurance/login.html", {"show_cabinet": False})


def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return render(
            request,
            "insurance/login.html",
            {
                "error_message": "You didnt enter a valid username and password.",
            },
        )
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request)
                return HttpResponse('<h1>Authenticated successfully</h1>')
            else:
                return HttpResponse('<h1>Disabled account</h1>')
        else:
            return HttpResponse('<h1>Invalid login</h1>')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                return HttpResponse("<h1>You are already registered</h1>")
            else:
                login(request, user)
                return redirect("")
    else:
        form = SignUpForm()
    return render(request, "insurance/signup.html", {'form': form})


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

