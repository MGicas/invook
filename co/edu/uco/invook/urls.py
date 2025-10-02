from .userinterface.api.controllers.inventory.HardwareController import HardwareController
from .userinterface.api.controllers.inventory.SupplyController import SupplyController
from .userinterface.api.controllers.resource.ConsumController import ConsumController
from .userinterface.api.controllers.resource.LoanController import LoanController   
from .userinterface.api.controllers.user.LenderController import LenderController
from . import views
from django.urls import path
from .userinterface.api.controllers.user.AdministrativeUserController import (
    AdministrativeUserListCreateAPIView,
    AdministrativeUserDetailAPIView,
    AdministrativeUserProfileAPIView,
    AdministrativeUserStateAPIView,
    AdministrativeUserRoleAPIView,
)
from .userinterface.api.controllers.user.LoginController import (
    AdminTokenObtainPairController, AdminTokenRefreshView, LogoutController, WhoAmIController
)
from .userinterface.api.controllers.resource.DailyStatisticsController import DailyStatisticsController
from .userinterface.api.controllers.inventory.RestockSupplyController import RestockSupplyController
from .userinterface.api.controllers.inventory.LowStockSupplyController import LowStockSupplyController
from .userinterface.api.controllers.notification.SendEmailController import SendEmailController

urlpatterns = [
    path('', views.home, name='home'), 
    path('inventory/hardware/', HardwareController.as_view()),  
    path('inventory/hardware/<str:serial>/', HardwareController.as_view()),

    # Supply
    path('inventory/supply/', SupplyController.as_view()),
    path('inventory/supply/<str:code>/', SupplyController.as_view()),
    path("inventory/supply/low-stock", LowStockSupplyController.as_view(), name="supplies-low-stock"),
    path("inventory/supply/<str:code>/restock/", RestockSupplyController.as_view(), name="supply-restock"), 

    # Consum
    path('consum/', ConsumController.as_view()),
    path('consum/<str:id>/', ConsumController.as_view()),

    # Loan
    path('loan/', LoanController.as_view()),
    path('loan/<str:id>/', LoanController.as_view()),
    path('statistics/', DailyStatisticsController.as_view(), name='daily-statistics'),
    
    path('users/lenders/', LenderController.as_view(), name='create-lender'),
    path('users/lenders/<str:id>/', LenderController.as_view()),

    path("users/admins/", AdministrativeUserListCreateAPIView.as_view(), name="adminuser-list-create"),
    path("users/admins/<int:pk>/", AdministrativeUserDetailAPIView.as_view(), name="adminuser-detail"),
    path("users/admins/<int:pk>/profile/", AdministrativeUserProfileAPIView.as_view(), name="adminuser-profile"),
    path("users/admins/<int:pk>/state/", AdministrativeUserStateAPIView.as_view(), name="adminuser-state"),
    path("users/admins/<int:pk>/role/", AdministrativeUserRoleAPIView.as_view(), name="adminuser-role"),

    path("auth/login/", AdminTokenObtainPairController.as_view(), name="auth-login"),
    path("auth/refresh/", AdminTokenRefreshView.as_view(), name="auth-refresh"),
    path("auth/logout/", LogoutController.as_view(), name="auth-logout"),
    path("auth/whoami/", WhoAmIController.as_view(), name="auth-whoami"),

    path('notification/send-email/', SendEmailController.as_view(), name='send-email'),
]