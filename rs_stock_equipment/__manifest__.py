# -*- coding: utf-8 -*-
{
    'name': 'Equipments in Inventory Transfers',

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """Functionalities:
Equipment Catalog:

There will be a catalog of all available equipment.
Add Equipment Selector to Inventory Transfers:

Include a selector for equipment in the inventory transfers.
Display Assigned Equipment in List View:

The list view should display the assigned equipment for each transfer.
Mandatory Equipment Selection:

Equipment selection will be mandatory. There will be an option "N/A" in the catalog for cases where no specific equipment applies.
Report on Transfers Related to Equipment:

Generate a report showing all inventory transfers related to a specific piece of equipment.
""",

    'author': 'Real Systems', 'maintainer': 'Carlos Contreras <carlosecv@realsystems.com.mx>',
    'website': 'https://www.realsystems.com.mx',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/rs_stock_equipment_data.xml',
        'views/stock_picking_views.xml',
        'views/rs_stock_equipment_views.xml',
        'views/stock_move_views.xml',
        'views/stock_move_line_views.xml',
        #'views/stock_quant_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

