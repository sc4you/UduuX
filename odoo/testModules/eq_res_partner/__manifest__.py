# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
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
    'name': "Equitania Kontakt Optimierungen",
    'license': 'AGPL-3',
    'version': '1.0.15',
    'category': 'Partner',
    'description': """Extensions for res_partner""",
    'author': 'Equitania Software GmbH',
    'summary': 'Partner Extension',
    'website': 'www.myodoo.de',
    "depends" : ['base', 'base_setup',"pragma_supplier_number", "pragma_customer_number"],
    'data': [
            "views/eq_res_partner_view.xml",
             ],
    "active": False,
    "installable": True
}
