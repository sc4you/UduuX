# -*- coding: utf-8 -*-
{
    'name': "UNITE Knowledge Base",

    'summary': """
        UNITE KB is a Knowledge Base and Manual/HowTo Management Module.
        """,

    'description': """
        comming soon
    """,

    'author': "UNITE",
    'website': "http://www.uniteit.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '2018.0.1',

    # any module necessary for this one to work correctly
    'depends': ['unite'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}