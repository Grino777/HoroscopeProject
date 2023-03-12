from django.http import HttpResponseNotFound, HttpResponseRedirect
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
    context = {
        "zodiacs": zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_zodiac_sign(request, sign_zodiac: str):
    context = {
        "sign": sign_zodiac.lower(),
        "description": zodiac_dict.get(sign_zodiac, None),
        "zodiacs": zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_zodiac_sign_by_number(request, sign_zodiac: int):
    if 1 <= sign_zodiac <= len(zodiac_dict):
        sign = list(zodiac_dict)[sign_zodiac-1]
        redirect_url = reverse('zodiac_sign', args=(sign,))
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Знака зодиака под номером {sign_zodiac} не существует!')

def get_type_elements(request):
    context = {
        'zodiac_elements': list(zodiac_element),
        "zodiacs": zodiac_dict,
    }
    return render(request, 'horoscope/elements_of_zodiac.html', context=context)

def get_signs_of_the_zodiac_element(request, element_type):
    zodiacs = zodiac_element.get(element_type, None)
    if zodiacs is None:
        zodiac_signs = None
    else:
        zodiac_signs = {sign: zodiac_dict.get(sign, None) for sign in zodiacs}
    context = {
        'zodiac_signs': zodiac_signs,
        'element_type': element_type,
        "zodiacs": zodiac_dict,
    }
    return render(request, 'horoscope/signs_of_element.html', context=context)