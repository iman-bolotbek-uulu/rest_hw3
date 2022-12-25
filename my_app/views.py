from django.shortcuts import render
import json
from . import models
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_good(request):
    if request.method == 'GET':
        goods = models.Good.objects.all()
        info = []
        for good in goods:
            info.append({'name': good.name, 'price': good.price, 'firm': good.firm.id, 'categories': good.categories.id})
        json_data = json.dumps(info)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        info = json.loads(request.body)
        new_good = models.Good.objects.create(**info)
        json_data = {'name': new_good.name, 'price': new_good.price, 'firm': new_good.firm.id, 'categories': new_good.categories.id}
        return JsonResponse(json_data, safe=False)


class GoodCreateListView(generics.ListCreateAPIView):
    queryset = models.Good.objects.all()
    serializer_class = serializers.GoodSerialize


class GoodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Good.objects.all()
    serializer_class = serializers.GoodSerialize


class GoodViewSet(viewsets.ModelViewSet):
    queryset = models.Good.objects.all()
    serializer_class = serializers.GoodSerialize


@csrf_exempt
def create_firm(request):
    if request.method == 'GET':
        firms = models.Company.objects.all()
        info = []
        for firm in firms:
            info.append({'name': firm.name, 'office': firm.office})
        json_data = json.dumps(info)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        info = json.loads(request.body)
        new_firm = models.Company.objects.create(**info)
        json_data = {'name': new_firm.name, 'office': new_firm.office}
        return JsonResponse(json_data, safe=False)


class CompanyCreateListView(generics.ListCreateAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerialize


class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerialize


@csrf_exempt
def create_category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        info = []
        for category in categories:
            info.append({'name': category.name})
        json_data = json.dumps(info)
        return JsonResponse(json_data, safe=False)
    if request.method == 'POST':
        info = json.loads(request.body)
        new_category = models.Category.objects.create(**info)
        json_data = {'name': new_category.name}
        return JsonResponse(json_data, safe=False)


# class CategoryCreateListView(generics.ListCreateAPIView):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerialize