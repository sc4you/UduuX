# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    © initOS GmbH 2016
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Website Canoncial URL",
    'summary': """
        Canonical URL in Website Headers
        """,
    'author': "initOS GmbH, Odoo Community Association (OCA), Equitania Software GmbH",
    'website': "http://www.initos.com & www.myodoo.de",
    'category': 'Website',
    'version': '10.0.1.0.2',
    'license': 'AGPL-3',
    'depends': [
        'website',
    ],
    'data': [
        'views/templates.xml',
    ],
}
