from application import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    body = db.Column(db.String(300), nullable=False)

    def __init__(self, title, subtitle,body):
        self.title = title
        self.subtitle = subtitle
        self.body = body