from odoo import models, fields, api

class Equipment(models.Model):
    _name = 'rs.stock.equipment'
    _description = 'Equipment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    code = fields.Char(string='Code', required=True)


    equipment_stock_move_line_count = fields.Integer(string='Stock Moves', compute='_compute_equipment_stock_move_line_count')

    equipment_stock_move_count = fields.Integer(string='Stock Moves', compute='_compute_equipment_stock_move_count')

    def _compute_equipment_stock_move_line_count(self):
        for record in self:
            record.equipment_stock_move_line_count = self.env['stock.move.line'].search_count([('equipment_id', '=', record.id)])


    def _compute_equipment_stock_move_count(self):
        for record in self:
            record.equipment_stock_move_count = self.env['stock.move'].search_count([('equipment_id', '=', record.id)])


    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.code}] {record.name}"
            result.append((record.id, name))
        return result

    @api.depends('name', 'code')
    def _compute_display_name(self):
        for template in self:
            template.display_name = False if not template.name else (
                '{}{}'.format(
                    template.code and '[%s] ' % template.code or '', template.name
                ))

    def action_view_stock_move_lines(self):
        self.ensure_one()
        action = self.env.ref('stock.stock_move_line_action').read()[0]
        action['domain'] = [('equipment_id', '=', self.id)]
        return action

    def action_view_stock_move(self):
        self.ensure_one()
        action = self.env.ref('stock.stock_move_action').read()[0]
        # Especificar la vista que quieres usar
        action['views'] = [(self.env.ref('stock.view_move_tree').id, 'tree'), (False, 'form')]

        action['domain'] = [('equipment_id', '=', self.id)]
        return action
