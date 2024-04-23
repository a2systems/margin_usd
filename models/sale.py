# Copyright 2020 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_margin_usd(self):
        for rec in self:
            res = 0
            res = rec.currency_id._convert(
                rec.margin,
                self.env.ref('base.USD'),
                rec.company_id,
                rec.date_order,
            )
            rec.margin_usd = res

    margin_usd = fields.Float('Margin USD',compute=_compute_margin_usd)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    def _compute_margins_usd(self):
        for rec in self:
            res = rec.order_id.currency_id._convert(
                rec.margin,
                self.env.ref('base.USD'),
                rec.order_id.company_id,
                rec.order_id.date_order,
            )
            rec.margin_usd = res
            res = rec.order_id.currency_id._convert(
                rec.purchase_price,
                self.env.ref('base.USD'),
                rec.order_id.company_id,
                rec.order_id.date_order,
            )
            rec.purchase_price_usd = res

    margin_usd = fields.Float('Margin USD',compute=_compute_margins_usd)
    purchase_price_usd = fields.Float('Purchase Price USD',compute=_compute_margins_usd)
