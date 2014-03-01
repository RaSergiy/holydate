#!/usr/bin/env python
# coding: utf-8

"""
holydate.cli
~~~~~~~~~~~~~

This module represent CLI interface of
holydate -- oldbeliever orthodox calendar.

:copyright: 2014 by Maxim Chernytevich.
:license: GPLv3, see LICENSE for more details.

"""

import sys
import textwrap
import argparse
from datetime import datetime
from pytils import translit
from holydate import AncientCalendar
from search_saints import search_saints


def main():

    def calendar(gr_day, gr_month, gr_year):
        """Print formatted calendar. """

        cal = AncientCalendar(gr_day, gr_month, gr_year)
        out = ''
        out += '\n\n' + \
            textwrap.fill(cal.getGrigorianDate(verbose='on'), initial_indent='  ', subsequent_indent='  ') + '\n' + \
            textwrap.fill(cal.getJulianDate(verbose='on'), initial_indent='  ', subsequent_indent='  ') + '\n\n' + \
            textwrap.fill(cal.getWeekday(verbose='on'), initial_indent='  ', subsequent_indent='  ') + '\n' +\
            textwrap.fill(cal.getTone(), initial_indent='  ', subsequent_indent='  ') + '\n\n' + \
            textwrap.fill(cal.getWeekdayname().format(red='\033[31m',  bold='\033[33m', end='\033[0m',
                          sx='ⵛ', gl='ⵛ', tw='⊕', pl='☩', redgui=''), width=100, initial_indent='  ', subsequent_indent='  ') + '\n\n' + \
            textwrap.fill(cal.getSaint().format(red='\033[31m', end='\033[0m', sx='ⵛ', gl='ⵛ',  pl='☩', tw='⊕', redgui=''),
                          width=100, initial_indent='  ', subsequent_indent='  ') + '\n\n' + \
            textwrap.fill(cal.getFast(), initial_indent='  ', subsequent_indent='  ') + '\n' +\
            textwrap.fill(cal.getBow(), width=110, initial_indent='  ', subsequent_indent='  ') + '\n\n'
        return out

    def search_constructor(string):
        """Construct command-line out."""

        result = search_saints(string)
        return result.format(red='\033[31m', end='\033[0m', sx='', gl='', pl='☩', tw='⊕', redgui='')


    def isodate(string):
        """Add new argparse type. Check date format."""
        try:
            return datetime.strptime(string, '%d-%m-%Y').date()
        except ValueError:
            msg = u'date input must in the format of dd-mm-yyyy'
            raise argparse.ArgumentTypeError(msg)

    def translit_cal(string):
        """Print transliterated formatted calendar. """

        try:
            out = string.replace('ⵛ', '-:)').replace('☩', '+').replace('⊕', '(+)')
            return translit.translify(out.decode('utf8'))
        except UnicodeDecodeError:
            return 'Transliteration is not working!'

    parser = argparse.ArgumentParser(description='Holydate, 0.1а1  ancient orthodox calendar.',
                                     epilog='Report bugs and wishes to <vechnoe.info@gmail.com>',
                                     prog='holydate',
                                     formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=127))
    parser.add_argument('translit', help='transliterate calendar output', nargs='?')
    parser.add_argument('-d', '--date', dest='date', action='store', type=isodate,
                        help='display a calendar for grigorian date input dd-mm-yyyy')
    parser.add_argument('-t', '--today', dest='today', action='store_true',
                        help='display a calendar for grigorian date today')
    parser.add_argument('-s', '--search', dest='string', action='store', type=str,
                        help='search saints and holidays in orthodoxy Menology')

    parser.add_argument('-v', '--version', action='version', version='Holydate version is 0.1а1')

    results = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
    elif results.today and results.translit:
        gr_day = datetime.today().day
        gr_month = datetime.today().month
        gr_year = datetime.today().year
        print translit_cal(calendar(gr_day, gr_month, gr_year))
    elif results.today:
        gr_day = datetime.today().day
        gr_month = datetime.today().month
        gr_year = datetime.today().year
        print calendar(gr_day, gr_month, gr_year)
    elif results.date and results.translit:
        gr_year = int(str(results.date)[:4])
        gr_month = int(str(results.date)[5:7])
        gr_day = int(str(results.date)[8:11])
        print translit_cal(calendar(gr_day, gr_month, gr_year))
    elif results.date:
        gr_year = int(str(results.date)[:4])
        gr_month = int(str(results.date)[5:7])
        gr_day = int(str(results.date)[8:11])
        print calendar(gr_day, gr_month, gr_year)
    elif results.string and results.translit:
        print '\n' + translit_cal(search_constructor(results.string))
    elif results.string:
        print '\n' + search_constructor(results.string)
    elif results.translit:
        parser.print_help()

if __name__ == "__main__":

    main()

