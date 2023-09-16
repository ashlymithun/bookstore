from odoo import models, fields


class Author(models.Model):
    _name = "bookstore.author"
    _description = "model for book's author"

    name = fields.Char("Author Name", required=True)
    image = fields.Binary(string="Image", attachment=False)
    book_ids = fields.One2many('bookstore.book','author_id',string="Books")
    description = fields.Text("Description")
    active = fields.Boolean(string="Active",default=True)

