from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://64.media.tumblr.com/74e5b17744ff959ee5cf5d443530e145/3974f37217a45119-98/s640x960/76f05a31040b80fd33aad9d90c842df298a42a08.jpg"

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__= "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age =  db.Column(db.Integer)
    notes =  db.Column(db.Text)
    available =  db.Column(db.Boolean, nullable=False, default=True)



    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or DEFAULT_IMAGE_URL
    
