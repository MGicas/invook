# interfaces/api/views/administrative_user_apiviews.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

from .....applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from .....applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from ...serializers.AdministrativeUserSerializer import (
    AdministrativeUserDetailSerializer,
    AdministrativeUserCreateSerializer,
    AdministrativeUserUpdateProfileSerializer,
    ChangeStateSerializer,
    SetRoleSerializer,
)

class AdministrativeUserListCreateAPIView(APIView):
    def __init__(self):
        self.administrative_facade = UserFacadeImpl()

    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = AdministrativeUser.objects.select_related("profile").all().order_by("id")
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        page = paginator.paginate_queryset(qs, request)
        if page is None:
            ser = AdministrativeUserDetailSerializer(page, many=True)
            return paginator.get_paginated_response(ser.data)
        
        ser = AdministrativeUserDetailSerializer(qs, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = AdministrativeUserCreateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        facade = self.administrative_facade
        user = facade.create_administrative_user(ser.to_dto())
        out = AdministrativeUserDetailSerializer(user)
        return Response(out.data, status=status.HTTP_201_CREATED)


class AdministrativeUserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk: int):
        user = get_object_or_404(
            AdministrativeUser.objects.select_related("profile"), pk=pk
        )
        return Response(AdministrativeUserDetailSerializer(user).data)


class AdministrativeUserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk: int):
        ser = AdministrativeUserUpdateProfileSerializer(data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        facade = self.administrative_facade
        user = facade.update_profile(pk, **ser.validated_data)
        return Response(AdministrativeUserDetailSerializer(user).data)


class AdministrativeUserStateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk: int):
        ser = ChangeStateSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        facade = self.administrative_facade
        user = facade.change_state(pk, ser.validated_data["state"])
        return Response(AdministrativeUserDetailSerializer(user).data)


class AdministrativeUserRoleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk: int):
        ser = SetRoleSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        facade = self.administrative_facade
        user = facade.set_role(pk, ser.validated_data["role"])
        return Response(AdministrativeUserDetailSerializer(user).data)
