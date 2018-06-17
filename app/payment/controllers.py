import hashlib
import requests
from flask import Blueprint, render_template, redirect, request, current_app, url_for, g, flash
from .forms import PaymentForm
from .models import Payment

module = Blueprint('payment', __name__, url_prefix='/payment')


def create_sign(data):
    sign = ':'.join([str(data[key]) for key in sorted(data.keys())]) + current_app.config['SECRET_KEY']
    sign_hash = hashlib.sha256(bytes(sign, 'utf-8')).hexdigest()
    return sign_hash


def create_data(keys):
    data = dict()
    for key in keys:
        if 'amount' in key:
            data[key] = g.form.data['amount']
        elif 'currency' in key:
            data[key] = current_app.config['CURRENCY_DICT'][g.form.data['currency']]
        elif key == 'shop_id':
            data[key] = current_app.config['SHOP_ID']
        elif key == 'shop_order_id':
            data[key] = current_app.config['SHOP_ORDER_ID']
        elif key == 'payway':
            data[key] = current_app.config['PAYWAY']
    data['sign'] = create_sign(data)
    return data


def pay_method():
    data = create_data(current_app.config['PAY_KEYS_REQUIRED'])
    g.form.save()
    return render_template('payment/pay_form.html', data=data)


def bill_method():
    data = create_data(current_app.config['BILL_KEYS_REQUIRED'])
    response = requests.post(current_app.config['BILL_URL'], json=data)
    if response.status_code == 200 and response.json()['result']:
        g.form.save()
        return redirect(response.json()['data']['url'])
    else:
        flash(response.json()['message'])
        return redirect(url_for('payment.payment'))


def invoice_method():
    data = create_data(current_app.config['INVOICE_KEYS_REQUIRED'])
    response = requests.post(current_app.config['INVOICE_URL'], json=data)
    if response.status_code == 200 and response.json()['result']:
        g.form.save()
        return render_template('payment/invoice_form.html', data=response.json()['data'])
    else:
        flash(response.json()['message'])
        return redirect(url_for('payment.payment'))


def set_form():
    g.form = PaymentForm(request.form)


@module.route('/', methods=['GET', 'POST'])
def payment():
    error = None
    set_form()
    if request.method == 'POST' and g.form.validate():
        if g.form.data['currency'] == current_app.config['EUR']:
            return pay_method()
        elif g.form.data['currency'] == current_app.config['USD']:
            return bill_method()
        elif g.form.data['currency'] == current_app.config['RUB']:
            return invoice_method()
        else:
            error = 'This currency is not supported.'
    payments = Payment.query.order_by(Payment.id.desc()).all()
    return render_template('payment/payment.html', error=error, payments=payments, form=g.form)
