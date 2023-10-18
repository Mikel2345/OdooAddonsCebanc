# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Productos(models.Model):
    _inherit = "product.template"

    list_price = fields.Float(
        'Sales Price', default=1.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.", required=True)

    @api.model
    def create(self, vals):
        for prod in self.env["product.template"].search([]):
            if prod.name == vals["name"]:
                raise ValidationError("Error. Ya hay un producto con ese nombre de artículo.")

        return super().create(vals)


class Pedidos(models.Model):
    _inherit = "sale.order"

    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: "[('groups_id', '=', {}), ('share', '=', False), ('company_ids', '=', company_id)]".format(
            self.env.ref("sales_team.group_sale_salesman").id
        ),required=True)

    def action_confirm(self):
        for line in self.order_line:
            for system_order in self.env["sale.order"].search([('partner_id','=',self.partner_id.id),('id','!=',self.id),('date_order','!=',self.date_order)]):
                raise ValidationError('Error. Es posible que estés duplicando un pedido previamente existente. Tienes que esperar 1 día después de la creación del pedido.')

        return super().action_confirm()


class transferencia(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        if self.scheduled_date < self.env['sale.order'].search([('name','=',self.origin)]).date_order:
            raise ValidationError('Error. La fecha de entrega no puede ser menor que la de fecha de pedido.')