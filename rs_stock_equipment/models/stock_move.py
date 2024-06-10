from odoo import models, fields

# class StockMove(models.Model):
#     _inherit = 'stock.move'

#     equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment', related='picking_id.equipment_id', store=True, readonly=False)

class StockMove(models.Model):
    _inherit = 'stock.move'

    equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment', related='picking_id.equipment_id', store=True, readonly=False)
