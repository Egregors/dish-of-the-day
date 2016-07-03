# -*- coding: utf8 -*-
from __future__ import unicode_literals, absolute_import
"""
    Каждую пятницу, я буду запускать этот скрипт, который бурет генерировать
    три случайные страны. И каждую субботу мы будем готовить какое-нибудь
    национальное блюды одной из полученныч стран, на выбор.

    @egregors 2016
"""
import re
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from random import choice

__version__ = '0.1'
__license__ = "Apache License v2.0"


def get_few_countries():
    # Получаем «сырой» список стран с Википедии
    # Мама, прости меня за это
    URL = ('https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D1%84%D0%B0%D0%B2'
           '%D0%B8%D1%82%D0%BD%D1%8B%D0%B9_%D1%81%D0%BF%D0%B8%D1%81%D0%B'
           'E%D0%BA_%D1%81%D1%82%D1%80%D0%B0%D0%BD_%D0%B8_%D1%82%D0%B5%D'
           '1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9?action=raw')
    raw_text = urllib2.urlopen(URL).read().decode('utf-8').split('\n')

    # Стркои с названиями стран начинаются с «#»
    raw_countries = [x for x in raw_text if x.startswith('#')]

    # Находим названия стран, используя регулярные выражения,
    # и немного колдунства
    countries = [x[0][1:-1] for x in [re.findall(
        '\|[а-яА-Яё ’,—-]+}', k) for k in raw_countries]]

    # Выбираем 3 случайные страны
    result = list()
    for x in range(3):
        result.append(choice(countries))

    return result

if __name__ == '__main__':
    print(get_few_countries())
