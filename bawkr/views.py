from django.http import JsonResponse
from django.views.generic import View
from bawkr.models import Bawk


class Bawks(View):
    def get(self, request):
        return JsonResponse({'bawks': [{
            'name': bawk.username,
            'message': bawk.message
        } for bawk in Bawk.objects.all()]})