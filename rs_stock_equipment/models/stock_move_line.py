from odoo import models, fields

# class StockMoveLine(models.Model):
#     _inherit = 'stock.move.line'

#     equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment', related='picking_id.equipment_id', store=True, readonly=False)
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment')
