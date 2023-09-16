from odoo import fields,models


class CustomerBookReport(models.AbstractModel):
    _name = "report.bookstore.report_customer_issued_book_report_template"
    _description = "Specific customer report"

    def _get_report_values(self, ids, data):
       # print("ids",ids[0])
       domain=[]
       domain +=[('id','=',ids[0])]
       books=[]
       result= self.env['bookstore.store'].search(domain)
       print("book",result)
       print("",result.name.name,result.date_of_issue)
       print("...",result.bookstore_ids)
       for x in result.bookstore_ids:
           books.append(
               {
                   'name':x.books_id.name,
                   'duration':x.duration,
                   'available':x.available,
                   'count':x.count,
                   'date_of_return':x.date_of_return
               }
           )

       return {
                   'customer': result.name.name,
                   'date_of_issue': result.date_of_issue,
                   'books':books
            }


