from rest_framework.response import Response
from hospital.models import *


def home(request):
    qs = User.objects.all()

    return Response(qs.data)
