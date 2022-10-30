# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Topaz Barcode',
    'version': '1.0',
    'summary': 'Editing Barcode ',
    'description': "",
    'website': 'http://topazsmart.com/',
    'depends': ['account', 'purchase', 'sale', 'stock','stock_barcode'],
    'sequence': -100,
    'data': [
        'views/stock_move_line_views.xml',
    ],
    'license': 'LGPL-3'

}
