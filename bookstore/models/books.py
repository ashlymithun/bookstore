from odoo import models, fields


class Book(models.Model):
    _name = "bookstore.book"
    _description = "book model"

    name = fields.Char("Book Name",required=True)
    author_id = fields.Many2one('bookstore.author',string="Author Name",required=True)
    category_id = fields.Many2one('bookstore.category',string="Category")
    quantity = fields.Integer(string="Number of Copies")
    tags_ids = fields.Many2many('bookstore.category',string="Tags")
    image = fields.Binary("Image")
    description = fields.Text("Description")
