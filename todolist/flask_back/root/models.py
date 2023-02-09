from . import db


class TodoFlask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    description = db.Column(db.Text)

    def __str__(self):
        return str(self.title)
