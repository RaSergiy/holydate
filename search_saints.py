#!/usr/bin/env python
# coding: utf-8

"""
Serach saints in menology.

"""

import re
import datetime
import textwrap
from menology import menology
from holydate_func import ju_to_gr_in_search

def search_saints(search_string):
    """Search saints in menology."""

    search_string = search_string.decode('utf8')
    d = menology
    out = []
    year = datetime.date.today().year
    pattern = re.compile(ur'{0}*'.format(search_string), re.I | re.U)

    #Ищем в menology строку; если есть, добавляем в out.
    for key, value in d.iteritems():
        for key1, value1 in d[key].iteritems():
            for key2, value2 in d[key][key1].iteritems():
                if re.search(pattern, str(value2).decode('utf8')):
                    out.extend([[ju_to_gr_in_search(key1, key, year), [key1, key], [value2]]])

    month_word = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }

    #Меняем элементы вложенного списка на значения словаря с названиями месяцев.
    for item in out:
        item[0][1], item[1][1] = month_word[item[0][1]], month_word[item[1][1]]

    string_out = ''

    #Вывод результата.
    if len(out) == 0:
        return 'Ваш запрос — «{}» не найден!'.decode('utf8').format(search_string)
    else:
        for item in out:
            string_out += textwrap.fill(str(item[0][0]).lstrip(), initial_indent='  ') \
                + '  ' + item[0][1] + ' по н. ст.' + '\n' + \
                textwrap.fill(str(item[1][0]), initial_indent='  ') \
                + '  ' + item[1][1] + ' по ст. ст.' + '\n' + \
                textwrap.fill(str(item[2][0]).format(red='\033[31m', end='\033[0m').lstrip(),
                              width=100, initial_indent='  ', subsequent_indent='  ') + '\n\n'
        return string_out

if __name__ == "__main__":

    search_string = raw_input('Input saint name >>> ')
    print search_saints(search_string)






















