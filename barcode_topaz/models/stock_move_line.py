import datetime

from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    topaz_m_expirationdate=fields.Char(string='Expiration Date')
    @api.onchange('product_id', 'product_uom_id', 'lot_name')
    def _onchange_product_id(self):
        if self.product_id:
            self.lot_name = self.product_id.topaz_lotname
            exdate = datetime.datetime.strptime(self.product_id.topaz_expiredate, '%d%m%y')
            self.expiration_date=exdate
            self.topaz_m_expirationdate=self.product_id.topaz_expiredate
            if self.picking_id:
                product = self.product_id.with_context(lang=self.picking_id.partner_id.lang or self.env.user.lang)
                self.description_picking = product._get_description(self.picking_id.picking_type_id)
            self.lots_visible = self.product_id.tracking != 'none'
            if not self.product_uom_id or self.product_uom_id.category_id != self.product_id.uom_id.category_id:
                if self.move_id.product_uom:
                    self.product_uom_id = self.move_id.product_uom.id
                else:
                    self.product_uom_id = self.product_id.uom_id.id
        else:
            self.lot_name=""
            self.topaz_m_expirationdate=""
            self.env.cr.execute(
                'update product_product set topaz_lotname=%s,topaz_expiredate=%s',
                ("", ""))
            self.env.cr.commit()

    @api.depends('product_id', 'picking_type_use_create_lots', 'lot_id.expiration_date')
    def _compute_expiration_date(self):
        for move_line in self:
            if move_line.lot_id.expiration_date:
                move_line.expiration_date = move_line.lot_id.expiration_date
            elif move_line.picking_type_use_create_lots:
                if move_line.product_id.use_expiration_date:
                    if not move_line.expiration_date:
                        if move_line.topaz_m_expirationdate:
                            exdate = datetime.datetime.strptime(self.topaz_m_expirationdate, '%d%m%y')
                            move_line.expiration_date = exdate
                        else:
                            move_line.expiration_date = fields.Datetime.today() + datetime.timedelta(
                                days=move_line.product_id.expiration_time)
                else:
                    move_line.expiration_date = False
    # super(SaleOrder, self).action_confirm()

