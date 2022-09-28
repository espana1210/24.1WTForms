from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, Length, URL

class AddPetForm(FlaskForm):
    name = StringField("Pets name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("rabbit", "Rabbit")])
    photo_url = StringField("Pets Photo", validators=[Optional(), URL()])
    age = IntegerField("How old?", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    #available = BooleanField("Available?", default=True)



class EditPetForm(FlaskForm):
    photo_url = StringField("Pets Photo", validators=[Optional(), URL()])
    
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
    