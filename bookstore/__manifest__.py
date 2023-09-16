{
    'name': 'Book Store',
    'version': '1.0',
    'category': 'uncategorized',
    'summary': 'Book_store',
    'description': """
This module contains all the common features of Book store.
    """,
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/bookstore_view.xml',
        'views/bookstore_category.xml',
        'views/bookstore_author.xml',
        'views/bookstore_book.xml',
        'views/search_records.xml',
        'wizards/sale_report_wizard.xml',
        'wizards/book_sale_report_wizard.xml',
        'reports/sale_report.xml',
        'reports/book_sale_report.xml',
        'reports/category_wise_book_report.xml',
        'reports/customer_book_issued_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': '2',
}