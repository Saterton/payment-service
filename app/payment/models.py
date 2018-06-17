from app.database import db


class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    currency = db.Column(db.String(3), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())

    def __str__(self):
        return 'Payment №%s' % self.id
