from datetime import datetime, timedelta

from odoo import api,models, fields
from odoo.exceptions import Warning


class Store(models.Model):
    _name = "bookstore.store"
    _description = "bookstore model"

    name = fields.Many2one('res.partner',string="Name of Customer",required=True)
    date_of_issue = fields.Date(string="Issued Date",default=datetime.today(),required=True)
    bookstore_ids = fields.One2many('bookstore.lines','bookstores_id',string="Books",required=True)


class StoreLines(models.Model):
    _name = "bookstore.lines"
    _description = "bookstore lines"

    books_id = fields.Many2one('bookstore.book',string="Book",required=True)
    duration = fields.Integer(string="Duration",required=True)
    count = fields.Integer(string="Count",default=1,required=True)
    bookstores_id = fields.Many2one('bookstore.store',string="Book Issue Details",required=True)
    date_of_return = fields.Date(string="Return Date",compute='_get_return_date',required=True)
    available = fields.Integer(string="Available",required=True,readonly=True)

    @api.onchange('books_id')
    def _get_book_quantity(self):
        if self.books_id:
            for rec in self:
                if rec.books_id.quantity >= 1:
                    x = rec.books_id.quantity
                    rec.available = x
                else:
                    raise Warning("book is not available")

    @api.onchange('count')
    def count_on_change(self):
        if self.available > 0 and (self.available < self.count):
            self.count = 0
            raise Warning("selected count is greater than available")
        if self.count > 3:
            raise Warning("count exceeds the limit (3)")

    @api.depends('duration')
    def _get_return_date(self):
        for rec in self:
            if rec.duration > 0:
                d1 = datetime.today()
                d2 = d1 + timedelta(days=rec.duration)
                rec.date_of_return = d2
            else:
                rec.date_of_return = ''

    def create(self, vals):
        res = super(StoreLines, self).create(vals)
        for i in res:
            # print("count", i.count)
            # print("count", i.books_id.quantity)
            current_stock = i.books_id.quantity - i.count
            # print("current quantity", current_stock)
            i.books_id.write({'quantity': current_stock})
        return res




