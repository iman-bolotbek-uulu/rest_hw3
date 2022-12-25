from rest_framework import serializers
from . import models


class GoodSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Good
        fields = "__all__"


class CompanySerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"


# class CategorySerialize(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = "__all__"
