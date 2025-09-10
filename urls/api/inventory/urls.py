from django.urls import path

from co.edu.uco.invook.userinterface.api.controllers.inventory.HardwareController import HardwareController
from co.edu.uco.invook.userinterface.api.controllers.inventory.SupplyController import SupplyController
from co.edu.uco.invook.userinterface.api.controllers.resource.ConsumController import ConsumController
from co.edu.uco.invook.userinterface.api.controllers.resource.LoanController import LoanController

urlpatterns = [
    # Hardware
    path('hardware/', HardwareController.as_view({'get': 'list', 'post': 'create'})),
    path('hardware/<str:serial>/', HardwareController.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),

    # Supply
    path('supply/', SupplyController.as_view({'get': 'list', 'post': 'create'})),
    path('supply/<str:code>/', SupplyController.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),

    # Consum
    path('consum/', ConsumController.as_view({'get': 'list', 'post': 'create'})),
    path('consum/<str:id>/', ConsumController.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),

    # Loan
    path('loan/', LoanController.as_view({'get': 'list', 'post': 'create'})),
    path('loan/<str:id>/', LoanController.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('loan/<str:id>/close/', LoanController.as_view({'post': 'close_loan'})), 
    path('loan/<str:id>/partial_return/', LoanController.as_view({'post': 'partial_return'})), 
]
