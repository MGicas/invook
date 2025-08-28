"""
URL configuration for invook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from co.edu.uco.invook.userinterface.api.controller.resource.LoanController import LoanController
from co.edu.uco.invook.userinterface.api.controller.resource.ConsumController import ConsumController
from co.edu.uco.invook.userinterface.api.controller.user.LenderController import LenderController
from co.edu.uco.invook.userinterface.api.controller.inventory.HardwareController import HardwareController
from co.edu.uco.invook.userinterface.api.controller.inventory.SupplyController import SupplyController
from co.edu.uco.invook.userinterface.api.controller.user.UserController import UserController
from co.edu.uco.invook.userinterface.api.controller.user.AdministrativeUserController import AdministrativeUserController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/loans/', LoanController.as_view()),               # GET y POST
    path('api/loans/<int:pk>/', LoanController.as_view()),      # DELETE
    path('api/consums/', ConsumController.as_view()),           # GET y POST
    path('api/consums/<int:pk>/', ConsumController.as_view()),      # DELETE
    path('api/lenders/', LenderController.as_view()),           # GET y POST
    path('api/lenders/<int:pk>/', LenderController.as_view()),      # DELETE
    path('api/hardwares/', HardwareController.as_view()),           # GET y POST
    path('api/hardwares/<int:pk>/', HardwareController.as_view()),      # DELETE
    path('api/supplys/', SupplyController.as_view()),           # GET y POST
    path('api/supplys/<int:pk>/', SupplyController.as_view()),      # DELETE
    path('api/user/', UserController.as_view()),           # GET y POST
    path('api/user/<int:pk>/', UserController.as_view()),      # DELETE
    path('api/administrativeUser/', AdministrativeUserController.as_view()),           # GET y POST
    path('api/administrativeUser/<int:pk>/', AdministrativeUserController.as_view()),      # DELETE
]
