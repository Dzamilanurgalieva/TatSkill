from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Главная страница"""
    return render(request, 'index.html')

def education(request):
    """Страница обучения"""
    return HttpResponse("Страница обучения (ЕГЭ, ВПР, Олимпиады)")

def travel(request):
    """Страница путешествий"""
    return HttpResponse("Страница поиска попутчиков по Татарстану")

def ratings(request):
    """Страница рейтингов"""
    return HttpResponse("Страница рейтингов учеников и путешественников")

def login(request):
    """Страница входа"""
    return HttpResponse("Страница входа")

def register(request):
    """Страница регистрации"""
    return HttpResponse("Страница регистрации")