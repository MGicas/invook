from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now

from co.edu.uco.invook.crosscutting.exception.ExceptionsBase import BadRequestException, ConflictException, NotFoundException

def ApiExceptions(exc, context):
    
    response = drf_exception_handler(exc, context)

    request = context.get("request")
    path = request.build_absolute_uri() if request else None

    def build_problem(status_code, detail, errors=None):
        problem = {
            "status": status_code,
            "title": status.HTTP_STATUS_CODES.get(status_code, "Error"),
            "detail": detail,
            "timestamp": now().isoformat(),
            "path": path,
        }
        if errors:
            problem["errors"] = errors
        return Response(problem, status=status_code)

    if isinstance(exc, NotFoundException):
        return build_problem(status.HTTP_404_NOT_FOUND, str(exc))

    if isinstance(exc, ConflictException):
        return build_problem(status.HTTP_409_CONFLICT, str(exc))

    if isinstance(exc, BadRequestException):
        return build_problem(status.HTTP_400_BAD_REQUEST, str(exc))

    if response is not None and response.status_code == 400:
        errors = []
        if isinstance(response.data, dict):
            for field, messages in response.data.items():
                if isinstance(messages, list):
                    for msg in messages:
                        errors.append({"field": field, "message": msg})
                else:
                    errors.append({"field": field, "message": messages})
        return build_problem(status.HTTP_400_BAD_REQUEST, "Error de validación.", errors)

    return build_problem(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error interno no esperado.")
