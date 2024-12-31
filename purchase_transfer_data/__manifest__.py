    'name': 'Purchase Transfer Data',
    'version': '18.0.1.0.0',',
    'category': 'Purchases',
    'summary': 'Transfer data from purchase order lines to stock picking lines',
    'description': """
        This module transfers data from purchase order lines to stock picking lines when a purchase order is confirmed.
    """,
    'author': 'Walter Falla Morales',
    'depends': ['purchase', 'stock'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,