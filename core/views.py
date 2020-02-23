from django.shortcuts import render
from django.http import JsonResponse


def test_view(request):
    data = {
        'name':'Soumya',
        'age': 35
    }
    return JsonResponse(data)