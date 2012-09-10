# -*- coding: utf-8 -*-
############################################################################################
#
#    Liferay CSV export to Excel CSV format.
#
#    Copyright (C) 2012 Enterprise Objects Consulting <http://www.eoconsulting.com.ar>
#    All Rights Reserved
#
#    Author: Mariano Ruiz <mr@eoconsulting.com.ar>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################################

import csv
from csv import Dialect

class LiferayDialect(Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

csv.register_dialect("liferayDialect", LiferayDialect)

cr = csv.reader(open("data.csv", "rb"), dialect="liferayDialect")
cw = csv.writer(open("clean_data.csv", "wb"), dialect="excel")

crlf = '\r\n'

for row in cr:
    row2 = []
    for col in row:
        while crlf in col or '\n' in col:
            col = col.replace(crlf, ' ')
            col = col.replace('\n', ' ')
        row2.append(col)
    cw.writerow(row2)

print "Finished"
