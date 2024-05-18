from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.log_in, name="login"),
    path("signup/", views.sign_up, name="signup"),
    path("logout/", views.log_out, name='logout'),
    path("<int:id>/", views.clients_cabinet, name="clients_cabinet"),
    path("<int:id>/contract_details/", views.contract_detail, name="contract_details"),
    path("<int:id>/make_order/", views.order_insurance, name="make_order"),
    path("<int:id>/change_personal_data/", views.change_personal_data, name="change_personal_data"),
]
