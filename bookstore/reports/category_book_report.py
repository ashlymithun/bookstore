from odoo import fields,models


class CategoryBookReport(models.AbstractModel):
    _name = "bookstore.category.report"
    _description = "category report"

    def category_report(self):
        domain = []
        books = []
        categories = []
        book = self.env['bookstore.book'].search(domain)
        category = self.env['bookstore.category'].search(domain)
        for x in category:
            categories.append({
                'id': x.id,
                'name': x.name
            })
        print("category",categories)
        for x in book:
            books.append({
                'name': x.name,
                'author': x.author_id.name,
                'description': x.description,
                'category_id': x.category_id.id
            })
            data ={
                'books': books,
                'categories': categories
            }
        return self.env.ref("bookstore.action_report_bookstore_category_book_report").report_action(self,data=data)


