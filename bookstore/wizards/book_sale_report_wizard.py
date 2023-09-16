from odoo import fields, models


class BookSaleReport(models.TransientModel):
    _name = "bookstore.book.sale.report"
    _description = "Book sale report"

    from_date = fields.Date(string="Start date")
    to_date = fields.Date(string="End date")
    categories_id = fields.Many2one('bookstore.category',string="Category")

    def get_report(self):
        domain = []
        books =[]
        book_list={}
        if self.categories_id:
            domain += [('books_id.category_id','=',self.categories_id.id)]
        if self.from_date:
            domain += [('bookstores_id.date_of_issue','>=',self.from_date)]
        if self.to_date:
            domain += [('bookstores_id.date_of_issue','<=',self.to_date)]
        result = self.env['bookstore.lines'].search(domain)
        for item in result:
            if item.books_id.id not in books:
                books.append(item.books_id.id)
                book_list[item.books_id.name] = item.count
            else:
                book_list[item.books_id.name] = int(book_list[item.books_id.name])+int(item.count)
        print("....",result)
        data = {
            'rec': book_list
        }
        return self.env.ref('bookstore.action_report_bookstore_book_sale').report_action(self, data=data)
