from rest_framework import status
from rest_framework.views import exception_handler

"""
Xatolik bo'lsa status 200 qaytadi
"""


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.status_code = status.HTTP_200_OK
    return response