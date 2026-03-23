from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .services.mistral_service import MistralService
from .models import Course, Community, Achievement

mistral_service = MistralService()


def home(request):
    """Главная страница"""
    # Получаем опубликованные курсы
    courses = Course.objects.filter(status='published').order_by('order', '-created_at')
    # Получаем активные сообщества
    communities = Community.objects.filter(is_active=True).order_by('order', 'name')
    # Получаем достижения
    achievements = Achievement.objects.filter(is_active=True)

    context = {
        'courses': courses,
        'communities': communities,
        'achievements': achievements,
    }
    return render(request, 'index.html', context)


def education(request):
    """Страница обучения"""
    courses = Course.objects.filter(status='published').order_by('order', '-created_at')
    return render(request, 'education.html', {'courses': courses})


def community(request):
    """Страница сообщества"""
    communities = Community.objects.filter(is_active=True).order_by('order', 'name')
    return render(request, 'community.html', {'communities': communities})


def ratings(request):
    """Страница рейтингов"""
    return HttpResponse("Рейтинги учеников - в разработке")


def login_view(request):
    """Страница входа"""
    return HttpResponse("Страница входа - в разработке")


def register_view(request):
    """Страница регистрации"""
    return HttpResponse("Страница регистрации - в разработке")


@csrf_exempt
@require_http_methods(["POST"])
def chat_api(request):
    """API для общения с Mistral AI"""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        conversation_history = data.get('history', [])

        if not user_message:
            return JsonResponse({'error': 'Сообщение не может быть пустым'}, status=400)

        result = mistral_service.get_response(user_message, conversation_history)

        if result['success']:
            return JsonResponse({
                'response': result['response'],
                'history': result['history']
            })
        else:
            return JsonResponse({'error': result['error']}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Неверный формат JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Внутренняя ошибка сервера: {str(e)}'}, status=500)