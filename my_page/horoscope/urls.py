from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type', views.get_type_elements),
    path('type/<str:element_type>', views.get_signs_of_the_zodiac_element, name='signs_of_the_zodiac_element'),
    path('<int:sign_zodiac>', views.get_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_zodiac_sign, name='zodiac_sign'),
]