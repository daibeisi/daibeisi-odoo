# -*- coding: utf-8 -*-
{
    'name': "示例插件",

    'summary': """示例插件，供copy和记各种用法""",

    'description': """
        示例插件，供copy和记各种用法。
    """,

    'author': "daibeisi",
    'website': "https://blog.bookhub.com.cn/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'diy',
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
