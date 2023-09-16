from odoo import api, models, fields


class Category(models.Model):
    _name = "bookstore.category"
    _description = "category model"
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name already Exists!')
    ]

    name = fields.Char("Category Name", required=True)
    description = fields.Text("Description")
    book_ids = fields.One2many('bookstore.book','category_id',string="Books")
    active = fields.Boolean("Active",default=True)
