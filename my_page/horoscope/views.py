from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs_list = list(zodiac_dict)
    # temp += f"<li><a href='{redirect_url}'>{sign.title()}</li>"
    context = {
        "zodiacs_list": zodiacs_list,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_zodiac_sign(request, sign_zodiac: str):
    context = {
        "sign": sign_zodiac.lower(),
        "description": zodiac_dict.get(sign_zodiac, None),
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_zodiac_sign_by_number(request, sign_zodiac: int):
    if 1 <= sign_zodiac <= len(zodiac_dict):
        sign = list(zodiac_dict)[sign_zodiac-1]
        redirect_url = reverse('zodiac_sign', args=(sign,))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Знака зодиака под номером {sign_zodiac} не существует!')

def get_type_elements(request):
    temp = ""
    for element in zodiac_element:
        redirect_url = reverse('signs_of_the_zodiac_element', args=(element,))
        temp += f"<li><a href='{redirect_url}'>{element.title()}</li>"
    response = f"<ul>{temp}</ul>"
    return HttpResponse(response)

def get_signs_of_the_zodiac_element(request, element_type):
    if element_type in zodiac_element:
        temp = ""
        for sign in zodiac_element[element_type]:
            redirect_url = reverse('zodiac_sign', args=(sign,))
            temp += f"<li><a href='{redirect_url}'>{sign.title()}</li>"
        response = f"<ul>{temp}</ul>"
        return HttpResponse(response)
    return HttpResponseNotFound(f"Такого типа элемента не существет - {element_type}")