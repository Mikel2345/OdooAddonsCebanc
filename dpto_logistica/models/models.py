# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class logistica(models.Model):
    _inherit = 'fleet.vehicle'

    @api.model
    def create(self,vals):
        ret=super().create(vals)

        fleet_ids = self.env['fleet.vehicle'].search([])
        for fleet in fleet_ids:
            if ret.driver_id != fleet.driver_id:
                if ret.driver_id.name == fleet.driver_id.name:
                    raise ValidationError('Error. El nombre del conductor está duplicado.')

                if ret.driver_id.phone == fleet.driver_id.phone:
                    raise ValidationError('Error. El número de teléfono del conductor está duplicado.')

                if ret.driver_id.email == fleet.driver_id.email:
                    raise ValidationError('Error. El correo del conductor está duplicado.')

        return ret


class misma_unidad(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for linea in self.order_line:
            for lineasec in self.order_line:
                if linea != lineasec:
                    if linea.product_id == linea.product_id:
                        if linea.product_uom != lineasec.product_uom:
                            raise ValidationError('Error. No puedes pedir 2 líneas del mismo producto con distinta unidad de medida.')

        return super().action_confirm()


class transportista_obligatorio(models.Model):
    _inherit = 'stock.picking'

    # carrier_id = fields.Many2one("delivery.carrier", string="Carrier", check_company=True, required=True)
    partner_id = fields.Many2one(
        'res.partner', 'Contact',
        check_company=True,
        states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},required=True)

