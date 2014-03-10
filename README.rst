========
holydate
========

Description
===========

This package represents the ancient Orthodox calendar for 
oldbelievers (better known as starovery or staroobryadts).
Containts name of weekday, julian and gregorian
dates, daily fasts and bows. Holydate contains search saints
and feasts in menology too.

Instalation
===========

From PYPI:

::

    pip install holydate


From repository:

::
   
    pip install https://github.com/vechnoe/holydate/zipball/master


Usage
=====

Holydate as python library:

::

   >>> from holydate import AncientCalendar

   >>> #Input grigorian day, month, year:
   >>> calendar = AncientCalendar(24, 01, 2014)
   >>> #Verbose mode on:
   >>> print calendar.getGrigorianDate(verbose='on')
   24 января 2014 года по н. ст.
   >>> print calendar.getJulianDate(verbose='on')
   11 января 2014 года по ст. ст.
   >>> print calendar.getWeekday(verbose='on')
   Пятница
   >>> print calendar.getTone()
   Глас пятый
   >>> print calendar.getWeekdayname()
   31 сeдмица по Пятидесятнице.
   >>> #Saint's string contains templates for color output
   >>> #and icons of feast's range.
   >>> print calendar.getSaint()
   Попраздненство Просвещения (6).
   {red}{pl} Преподобнаго и богоноснаго отца нашего,
   Феодосия общему житию начальника (Пл.).
   {pl} И память преподобнаго отца нашего Михаила
   Клопскаго Новгородскаго чудотворца (Пл.).{end}
   Прп. отца нашего Феодосия, иже от Антиохии.
   >>> #Fasts and bows.
   >>> print calendar.getFast()
   Пища с рыбой.
   >>> print calendar.getBows()
   Приходные и исходные поклоны поясные.


Holydate as utility with command-line interface:

::

    user@localhost:~$ holydate
    usage: holydate [-h] [-d DATE] [-t] [-s STRING] [-v] [translit]

    Holydate, 0.1 ancient orthodox calendar.

    positional arguments:
      translit                    transliterate calendar output

    optional arguments:
      -h, --help                  show this help message and exit
      -d DATE, --date DATE        display a calendar for grigorian date input dd-
                                  mm-yyyy
      -t, --today                 display a calendar for grigorian date today
      -s STRING, --search STRING  search saints and holidays in orthodoxy Menology
      -v, --version               show program's version number and exit

    Report bugs and wishes to <vechnoe.info@gmail.com>

::

    user@localhost:~$ holydate -t


    24 января 2014 года по н. ст.
    11 января 2014 года по ст. ст.

    Пятница
    Глас пятый

    31 сeдмица по Пятидесятнице.

    Попраздненство Просвещения (6). ☩ Преподобнаго и
    богоноснаго отца нашего, Феодосия общему житию
    начальника (Пл.). ☩ И память преподобнаго отца нашего
    Михаила Клопскаго Новгородскаго чудотворца (Пл.).
    Прп. отца нашего Феодосия, иже от Антиохии.

    Пища с рыбой.
    Приходные и исходные поклоны поясные.

::

    user@localhost:~$ holydate -d 26-01-2014

    26 января 2014 года по н. ст.
    13 января 2014 года по ст. ст.

    Воскресенье
    Глас шестой

    Неделя по Просвещении. 31 неделя по Пятидесятнице
    (Пл.).

    ⵛ Попраздненство Просвещения (6). Святых мученник
    Ермила и Стратоника (4). В сий день поется служба
    святых отец избиенных  в Синаи, и в Раифе (4). Св. мч.
    Петра Анейскаго. Прп. отца нашего Иякова, иже от
    Нисивии. Прп. отца нашего Елеазара Анзерскаго. Прп.
    отца нашего Иринарха Затворника, Ростовскаго
    чудотворца.

    Пища скоромная.
    Приходные и исходные поклоны поясные.


::

    maximus@localhost:~/Desktop/workspace$ holydate -d 26-01-2014 translit

    26 yanvarya 2014 goda po n. st.
    13 yanvarya 2014 goda po st. st.

    Voskresen'e
    Glas shestoj

    Nedelya po Prosveschenii. 31 nedelya po Pyatidesyatnitse
    (Pl.).

    -:) Poprazdnenstvo Prosvescheniya (6). Svyatyih muchennik
    Ermila i Stratonika (4). V sij den' poetsya sluzhba
    svyatyih otets izbiennyih  v Sinai, i v Raife (4). Sv. mch.
    Petra Anejskago. Prp. ottsa nashego Iyakova, izhe ot
    Nisivii. Prp. ottsa nashego Eleazara Anzerskago. Prp.
    ottsa nashego Irinarha Zatvornika, Rostovskago
    chudotvortsa.

    Pischa skoromnaya.
    Prihodnyie i ishodnyie poklonyi poyasnyie.

Serarch saints and feasts in all year:

::

    user@localhost:~$ holydate -s Амвросия

    11  ноября по н. ст.
    29  октября по ст. ст.
    ☩ Иже во свв. отца нашего и исповедника Амвросия,
    митрополита Белокриницкаго (Бд.).

    20  декабря по н. ст.
    7  декабря по ст. ст.
    Иже во свв. отца нашего Амвросия, еп. Медиоламскаго (4)
    (Алл.). ☩ Преставление прп. отца нашего Антония
    Сийскаго, новаго чудотворца (Бд.).


Authors
=======

* Author: `Maxim Chernyatevich`_

.. _`Maxim Chernyatevich`: https://github.com/vechnoe


Dependencies
============

*Required*

* `Python 2.7.x. <http://python.org/download/>`_

*Optional*

* `Pytils <https://pypi.python.org/pypi/pytils/>`_ (required for the `translit` option in CLI interface)


License
=======

Copyright 2013-2014 Maxim Chernyatevich (http://www.vechnoe.info)

`GNU General Public License v3 or later <http://www.gnu.org/licenses/>`_


