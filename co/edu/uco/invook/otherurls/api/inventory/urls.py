from django.urls import path

from co.edu.uco.invook.userinterface.api.controllers.inventory.HardwareController import HardwareController
from co.edu.uco.invook.userinterface.api.controllers.inventory.SupplyController import SupplyController
from co.edu.uco.invook.userinterface.api.controllers.resource.ConsumController import ConsumController
from co.edu.uco.invook.userinterface.api.controllers.resource.LoanController import LoanController

urlpatterns = [
    # Hardware
    path('hardware/', HardwareController.as_view()),
    path('hardware/<str:serial>/', HardwareController.as_view()),

    # Supply
    path('supply/', SupplyController.as_view()),
    path('supply/<str:code>/', SupplyController.as_view()),

    # Consum
    path('consum/', ConsumController.as_view()),
    path('consum/<str:id>/', ConsumController.as_view()),

    # Loan
    path('loan/', LoanController.as_view()),
    path('loan/<str:id>/', LoanController.as_view()),
    path('loan/<str:id>/close/', LoanController.as_view()), 
    path('loan/<str:id>/partial_return/', LoanController.as_view()), 
]
