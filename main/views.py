from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Главная страница"""
    return render(request, 'index.html')

def education(request):
    """Страница обучения"""
    return render(request, 'skill.html')

def travel(request):
    """Страница путешествий"""
    return render(request, 'trips.html')

def ratings(request):
    """Страница рейтингов"""
    return HttpResponse("Страница рейтингов учеников и путешественников")

def login(request):
    """Страница входа"""
    return HttpResponse("Страница входа")

def register(request):
    """Страница регистрации"""
    return HttpResponse("Страница регистрации")