from app.database import db
from settings import EUR, USD, RUB
from wtforms import Form, TextAreaField, FloatField, SelectField
from wtforms.validators import data_required, length
from .models import Payment


class PaymentForm(Form):
    currency_choices = (
        (EUR, EUR),
        (USD, USD),
        (RUB, RUB)
    )

    amount = FloatField('Payment amount', validators=[data_required()])
    currency = SelectField('Currency', validators=[data_required(), length(max=3)], choices=currency_choices)
    description = TextAreaField('Description', validators=[length(max=1024)], render_kw={'rows': 10, 'cols': 50})

    def save(self):
        payment = Payment(**self.data)
        db.session.add(payment)
        db.session.commit()
        return payment
