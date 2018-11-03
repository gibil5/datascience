# -*- coding: utf-8 -*-
{
    'name': "datascience",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """

        3 Nov 2018

    """,

    'author': "J. Revilla",
    
    'website': "www.jrevilla.com",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],



    # always loaded
    'data': [

        #'views/views.xml',
        #'views/templates.xml',

        #'views/riders.xml',
        #'views/rider_lines.xml',

        #'views/menus.xml',
    ],



    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}