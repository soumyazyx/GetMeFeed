from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name':'Soumya',
            'age': 35
        }
        return Response(data)


# def test_view(request):
#     data = {
#         'name':'Soumya',
#         'age': 35
#     }
#     return JsonResponse(data)