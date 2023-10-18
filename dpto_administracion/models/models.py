# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class delegacion_unica(models.Model):
    _inherit = 'res.company'

    street = fields.Char(compute='_compute_address', inverse='_inverse_street', required=True)
    phone = fields.Char(related='partner_id.phone', store=True, readonly=False, required=True)
    email = fields.Char(related='partner_id.email', store=True, readonly=False, required=True)


    @api.model
    def create(self,vals):
        for c in self.env["res.company"].search([]):
            if c.phone==vals["phone"]:
                raise ValidationError("Error. Ya hay una delegación con ese número de teléfono.")
            if c.street==vals["street"]:
                raise ValidationError("Error. Ya hay una delegación en esa calle.")
            if c.email==vals["email"]:
                raise ValidationError("Error. Ya hay una delegación con ese correo electrónico.")

        return super().create(vals)

class departamento_unico(models.Model):
    _inherit = 'hr.department'


    manager_id = fields.Many2one('hr.employee', string='Manager', tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",required=True)

    @api.model
    def create(self, vals):
        for c in self.env["res.company"].search([()]):
            for d in self.env["hr.department"].search([('company_id', '=', c.id)]):
                if d.manager_id.id==vals["manager_id"]:
                    raise ValidationError("Error. Ya hay un departamento con ese gerente.")


        return super().create(vals)