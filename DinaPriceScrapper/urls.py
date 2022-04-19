from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from scraping import get_products
from datetime import datetime
from django.http import HttpResponseRedirect
from .views import home

urlpatterns = [
    path("", home),
]
