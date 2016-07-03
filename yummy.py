# -*- coding: utf8 -*-
from __future__ import unicode_literals, absolute_import
"""
    Каждую пятницу, я буду запускать этот скрипт, который бурет генерировать
    три случайные страны. И каждую субботу мы будем готовить какое-нибудь
    национальное блюды одной из выпавших стран, на выбор.

    @egregors 2016
"""
import re
from urllib import request
from random import choice

__version__ = '0.2'
__license__ = "Apache License v2.0"


def log(msg=None):
    if msg:
        print('[YUMMY]: {}'.format(msg))


def get_few_countries():
    """
    """
    cat = """\n
    yammy.py     /\_/\ 
            ____/ o o \ 
          /~____  =ø= / 
         (______)__m_m) 
    """
    log(cat)
    log('Самое время выбрать страны на эти выходные!')

    # Получаем «сырой» список стран с Википедии
    # Мама, прости меня за это
    log('Получаю список стран..')
    log('.')
    URL = ('https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D1%84%D0%B0%D0%B2'
           '%D0%B8%D1%82%D0%BD%D1%8B%D0%B9_%D1%81%D0%BF%D0%B8%D1%81%D0%B'
           'E%D0%BA_%D1%81%D1%82%D1%80%D0%B0%D0%BD_%D0%B8_%D1%82%D0%B5%D'
           '1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9?action=raw')
    raw_text = request.urlopen(URL).read().decode('utf-8').split('\n')

    # Стркои с названиями стран начинаются с «#»
    raw_countries = [x for x in raw_text if x.startswith('#')]

    # Находим названия стран, используя регулярные выражения,
    # и немного колдунства
    countries = [x[0][1:-1] for x in [re.findall(
        '\|[а-яА-Яё ’,—-]+}', k) for k in raw_countries]]

    # Выбираем 3 случайные страны
    log('На этой неделе у нас:')
    result = list()
    while len(result) < 3:
        country = choice(countries)
        if country not in result:
            result.append(country)

    log('+--------------------+')
    for idx, country in enumerate(result):
        log(' {}. {}'.format(idx + 1, country))
    log('+--------------------+')


if __name__ == '__main__':
    get_few_countries()
