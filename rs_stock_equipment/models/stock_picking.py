from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.model
    def _default_equipment_id(self):
        try:
            rec = self.env.ref('rs_stock_equipment.equipment_na')
            return rec.id
        except ValueError:
            return False

    equipment_id = fields.Many2one('rs.stock.equipment', string='Equipment', required=False, default=lambda self: self._default_equipment_id())


    # def write(self, vals):
    #     res = super(StockPicking, self).write(vals)
    #     if 'equipment_id' in vals:
    #         for picking in self:
    #             picking.move_ids.write({'equipment_id': vals['equipment_id']})
    #             picking.move_line_ids.write({'equipment_id': vals['equipment_id']})
    #     return res

    # @api.model
    # def create(self, vals):
    #     picking = super(StockPicking, self).create(vals)
    #     if 'equipment_id' in vals:
    #         picking.move_ids.write({'equipment_id': vals['equipment_id']})
    #         picking.move_line_ids.write({'equipment_id': vals['equipment_id']})
    #     return picking
