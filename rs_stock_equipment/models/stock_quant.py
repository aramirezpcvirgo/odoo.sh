from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment', compute='_compute_equipment_id')

    def _compute_equipment_id(self):
        for quant in self:
            move_lines = self.env['stock.move.line'].search([('lot_id', '=', quant.lot_id.id)], limit=1)
            quant.equipment_id = move_lines.equipment_id if move_lines else False
