from .userinterface.api.controllers.inventory.HardwareController import HardwareController
from .userinterface.api.controllers.inventory.SupplyController import SupplyController
from .userinterface.api.controllers.resource.ConsumController import ConsumController
from .userinterface.api.controllers.resource.LoanController import LoanController   
from .userinterface.api.controllers.user.AdministrativeUserController import AdministrativeUserController
from .userinterface.api.controllers.user.LenderController import LenderController
from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'), 
    path('inventory/hardware/', HardwareController.as_view()),  
    path('inventory/hardware/<str:serial>/', HardwareController.as_view()),
    path('inventory/hardware/<str:serial>/mark_available/', HardwareController.as_view(), name='patch-hardware-available'),  # PATCH marcar disponible
    path('inventory/hardware/<str:serial>/mark_unavailable/', HardwareController.as_view(), name='patch-hardware-unavailable'),  # PATCH marcar no disponible

    # Supply
    path('inventory/supply/', SupplyController.as_view()),
    path('inventory/supply/<str:code>/', SupplyController.as_view()),

    # Consum
    path('consum/', ConsumController.as_view()),
    path('consum/<str:id>/', ConsumController.as_view()),

    # Loan
    path('loan/', LoanController.as_view()),
    path('loan/<str:id>/', LoanController.as_view()),
    path('loan/<str:id>/close/', LoanController.as_view()), 
    path('loan/<str:id>/partial_return/', LoanController.as_view()), 
    
    path('users/lenders/', LenderController.as_view(), name='create-lender'),
    path('users/lenders/<str:id>/', LenderController.as_view()),

    path('users/admins/', AdministrativeUserController.as_view()),
    path('users/admins/<str:id>/', AdministrativeUserController.as_view()),
]