# -*- coding: utf-8 -*-
{
    'name': "document_module",
    'summary': "Module for storing information",
    'description': """
Module for storing information about documents or books.
    """,
    'author': "Eimantas",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'depends': [
        'base',
    ],
    'data': [
        'views/views.xml',
        #'views/wizard_views.xml',
        'data/actions.xml',
        'data/ir.model.access.csv',
        'data/menu_views.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
