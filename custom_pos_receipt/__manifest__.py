# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "custom POS Receipt Topaz",
    'version': '15.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'summary': 'Customized Receipt of Point Of Sales Topaz',
    'description': ""
                   "Customized Receipt of Point Of Sales Topaz"
                   "",
    'depends': ['point_of_sale'],
    'data': [
        # 'views/res_partner_form.xml'
    ],
    'assets': {
        'web.assets_qweb': [
            'custom_pos_receipt/static/src/xml/pos_receipt.xml',
        ],
        'web.assets_backend': [
            'custom_pos_receipt/static/src/js/pos_receipt.js',
        ],
    },
    # 'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
