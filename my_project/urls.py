"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('good_set', views.GoodViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', views.create_category),
    path('api/firm/', views.create_firm),
    path('api/good/', views.create_good),
    path('api/v-0.1/firm/', views.CompanyCreateListView.as_view()),
    path('api/v-0.1/firm/<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v-0.1/good/', views.GoodCreateListView.as_view()),
    path('api/v-0.1/good/<int:pk>/', views.GoodRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v-0.2/', include(router.urls)),
]
