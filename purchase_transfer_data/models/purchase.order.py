from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    contenedor = fields.Char(string='Traza')

class StockMove(models.Model):
    _inherit = 'stock.move'

    contenedor = fields.Char(string='Traza Contenedor')

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            for line in order.order_line:
                # Actualizamos los movimientos de stock relacionados
                moves = self.env['stock.move'].search([
                    ('purchase_line_id', '=', line.id),
                    ('state', 'not in', ['cancel', 'done'])
                ])
                if moves:
                    moves.write({
                        'contenedor': line.contenedor
                    })
                
                # Actualizamos las líneas de recepción (stock.picking)
                for picking in order.picking_ids:
                    picking_moves = picking.move_lines.filtered(
                        lambda m: m.purchase_line_id.id == line.id and 
                        m.state not in ['cancel', 'done']
                    )
                    if picking_moves:
                        picking_moves.write({
                            'contenedor': line.contenedor
                        })
        return res