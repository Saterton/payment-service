import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = 'SecretKey01'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'db.sqlite3')

SHOP_ID = 5
SHOP_ORDER_ID = 1
PAYWAY = 'payeer_rub'

EUR = 'EUR'
USD = 'USD'
RUB = 'RUB'

EUR_ISO_CODE = 978
USD_ISO_CODE = 840
RUB_ISO_CODE = 643

PAY_URL = 'https://pay.piastrix.com/ru/pay'
BILL_URL = 'https://core.piastrix.com/bill/create'
INVOICE_URL = 'https://core.piastrix.com/invoice/create'

PAY_KEYS_REQUIRED = ['amount', 'currency', 'shop_id', 'shop_order_id']
BILL_KEYS_REQUIRED = ['shop_amount', 'shop_currency', 'shop_id', 'shop_order_id', 'payer_currency']
INVOICE_KEYS_REQUIRED = ['amount', 'currency', 'payway', 'shop_id', 'shop_order_id']

CURRENCY_DICT = {
    EUR: EUR_ISO_CODE,
    USD: USD_ISO_CODE,
    RUB: RUB_ISO_CODE,
}

try:
    from local_settings import *
except ImportError:
    pass
