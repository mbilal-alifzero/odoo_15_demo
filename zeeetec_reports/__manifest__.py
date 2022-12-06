# -*- encoding: utf-8 -*-
{
	"name": "Zeeetec Customized Reports",
	"summary": "Zeeetec Customized Reports",
	"description": """

	""",
	"version": "15.0",
	"category": "Reports",
	"author": "Muhammad Bilal",
	"website": "http://www.odoo.com",
	"depends": ["zeeetec_customization", "sale", "account", "stock"],
	"license": 'LGPL-3',
    'support': 'Muhammad Bilal mbilal4m@gmail.com',
	"data": [
		# 'security/ir.model.access.csv',
		'views/client_order_reports.xml',
		# 'views/sale_order_reports.xml',
		'views/delivery_order_reports.xml',
		],
	"auto_install": False,
	"installable": True,
	"application": False,
}
