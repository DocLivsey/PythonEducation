from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("<int:id>/", views.clients_cabinet, name="clients_cabinet"),
    path("<int:id>/contract_details/", views.contract_detail, name="contract_details"),
    path("<int:id>/make_order", views.order_insurance, name="make_order"),

]
