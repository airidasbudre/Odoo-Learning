# -*- coding: utf-8 -*-
{
    'name': "Product Notebook",

    'summary': """
        New pages to product notebook. List view progress bars""",

    'description': """
        Task
    """,

    'author': "Airidas",
    'website': "https://www.pakelkdrona.lt/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
          'views/product_notebook_add.xml',
    ],
}