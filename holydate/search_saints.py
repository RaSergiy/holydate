#!/usr/bin/env python
# coding: utf-8

"""
Serach saints and feasts in year menology.

"""

import re
import datetime
import calendar
import textwrap
from menology import menology
from holydate import AncientCalendar
from holydate_func import ju_to_gr_in_search, gr_to_ju_in_search


def search_saints(search_string, mode='text'):
    """Search saints and feasts in year menology.
    :param search_string: search input string (e.g. saint name).
    :param mode: text or html.
    """

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

    search_string = search_string.decode('utf8')
    year = datetime.date.today().year
    year_menology = menology
    cal_out = []
    
    #List of weekday names.
    for month in range(1, 13):
        days_in_month = calendar.monthrange(year, month)[1]
        for day in range(1, days_in_month + 1):
            cal = AncientCalendar(day, month, year)
            weekdayname = cal.getWeekdayname()
            cal_out.extend([[gr_to_ju_in_search(day, month, year), weekdayname]])

    for i in cal_out:
        year_menology[i[0][1]][i[0][0]]['weekday'] = i[1]

    d = year_menology
    out = []
    pattern = re.compile(ur'{0}*'.format(search_string), re.I | re.U)

    #Ищем в menology строку; если есть, добавляем в out.
    for key, value in d.iteritems():
        for key1, value1 in d[key].iteritems():
            for key2, value2 in d[key][key1].iteritems():
                if re.search(pattern, str(value2).decode('utf8')):
                    out.extend([[ju_to_gr_in_search(key1, key, year), [key1, key], [value2]]])

    #Меняем элементы вложенного списка на значения словаря с названиями месяцев.
    for item in out:
        item[0][1], item[1][1] = month_word[item[0][1]], month_word[item[1][1]]

    string_out = ''

    #Вывод результата.
    if len(out) == 0:
        return 'Ваш запрос — «{}» не найден!'.decode('utf8').format(search_string)
    elif mode == 'text':
        for item in out:
            string_out += textwrap.fill(str(item[0][0]).lstrip(), initial_indent='  ') \
                + '  ' + item[0][1] + ' по н. ст.' + '\n' + \
                textwrap.fill(str(item[1][0]), initial_indent='  ') \
                + '  ' + item[1][1] + ' по ст. ст.' + '\n' + \
                textwrap.fill(str(item[2][0]).lstrip(),
                              width=100, initial_indent='  ', subsequent_indent='  ') + '\n\n'
        return string_out
    elif mode == 'html':
        for item in out:
            string_out += '<span class="date">' + str(item[0][0]) + ' ' + item[0][1] + ' по н. ст.' + '<br>' + '\n' +\
                          str(item[1][0]) + ' ' + item[1][1] + ' по ст. ст.' + '</span>' + '<br>' + '\n' +\
                          '<span class="saint">' + str(item[2][0]).rstrip() + '\n' + '</span>' + '<br><br>' + '\n\n'
        return string_out


if __name__ == "__main__":

    search_string = raw_input('Input saint name >>> ')
    print search_saints(search_string, mode='text')

