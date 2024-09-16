# -*- coding: utf-8 -*-
{
    'name': "Residence Management",

    'summary': """
        Residence management project.""",

    'description': """
        Residence management project.
    """,

    'author': "Binhex,Odoo Community Association (OCA)",
    'website': "https://github.com/tegin/medical-fhir/tree/16.0",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','medical_base','project','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/residence_views.xml',

    ],
}
