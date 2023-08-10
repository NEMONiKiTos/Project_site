from django.http import HttpResponse
from django.shortcuts import render


def index(requests):
    return HttpResponse("Домашка по 4 занятию")