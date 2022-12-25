from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=30)
    office = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    firm = models.ForeignKey(Company, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


