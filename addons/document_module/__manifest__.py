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
    'depends': ['base'],
    'application': True,
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/actions.xml',
        'data/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
