from django.urls import path
from co.edu.uco.invook.userinterface.api.controllers.user.LenderController import LenderController
from co.edu.uco.invook.userinterface.api.controllers.user.AdministrativeUserController import AdministrativeUserController

urlpatterns = [
    path('lenders/', LenderController.as_view(), name='create-lender'),
    path('lenders/<str:id>/', LenderController.as_view()),

    path('admins/', AdministrativeUserController.as_view()),
    path('admins/<str:id>/', AdministrativeUserController.as_view()),
]
