from django.shortcuts import render
from .raspiberry import light


def index(request):
    context = {}
    context['title'] = 'Smart Home'
    context['hello'] = 'Hello World'
    return render(request, 'index.html', context)


def light_on(request):
    context = {}
    context['light'] = '点亮'
    context['success'] = light(1)
    return render(request, 'light.html', context)


def light_off(request):
    context = {}
    context['light'] = '熄灭'
    context['success'] = light(0)
    return render(request, 'light.html', context)


def led(request):
    s = int(request.GET['light'])
    light(s)
    return render(request, 'light.html')