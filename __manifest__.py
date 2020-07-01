# -*- coding: utf-8 -*-
{
    'name': "Pretty Mail",
    'summary': """Improved appearance for the mail module, visual effects in the style of whatsapp""",
    'author': "Kirill Sudnikovich",
    'website': "https://sntch.dev",
    'category': 'Uncategorized',
    'version': '13.0.3.0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_config_settings_views.xml',
    ],
    'qweb': [
        'static/src/xml/thread.xml',
    ],
}
