# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta,datetime


class recursos_humanos(models.Model):
    _inherit = 'hr.leave'

    @api.model
    def create(self,vals):
        if vals["number_of_days"]>10:
            raise ValidationError("Error. El límite de las vacaciones son 2 semanas.")

        # for c in self.env["hr.leave"].search([]):
        #     if c.department_id.id == vals["department_id"] and c.state=='validate':
        #         if (c.request_date_from <= datetime.strptime(vals["request_date_to"],'%Y-%m-%d').date()) and (c.request_date_to >= datetime.strptime(vals["request_date_from"],'%Y-%m-%d').date()):
        #             raise ValidationError("Error. Ya hay una persona con vacaciones en esas fechas.")


        ret=super().create(vals)
        for c in self.env["hr.leave"].search([]):
            if c.department_id.id == ret.department_id.id and c.state=='validate':
                if (c.request_date_from <= ret.request_date_to) and (c.request_date_to >= ret.request_date_from):
                    raise ValidationError("Error. Ya hay una persona con vacaciones en esas fechas.")



        return ret


class contratos(models.Model):
    _inherit = 'hr.contract'

    first_contract_date = fields.Date(related='employee_id.first_contract_date', required=True)
    date_start = fields.Date('Start Date', required=True, default=fields.Date.today, tracking=True,
        help="Start date of the contract.")



    @api.model
    def create(self,vals):
        ret = super().create(vals)

        if ret.date_start < (fields.Date.today() - timedelta(days=10)):
            raise ValidationError("Error. La fecha de inicio de contrato no puede ser 10 días anterior que la fecha actual.")

        for c in self.env["hr.contract"].search([]):
            if c.employee_id.id == ret.employee_id.id and c.state == 'open':
                if (c.date_start <= ret.date_end) and (c.date_end >= ret.date_start):
                    raise ValidationError("Error. Esa persona ya tiene un contrato entre esas fechas.")

        return ret
