# -*- coding: utf-8 -*-
{
    'name': "Health Care Base",

    'summary': """
        Module needed by all Health Care modules.""",

    'description': """
        Contains: FHIR Complex Types, common definitions
    """,

    'author': "Luigi Sison",
    'website': "https://hl7-fhir.github.io/datatypes.html",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health Care',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
}