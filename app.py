from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "OH-SECRET"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)




connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    return render_template('base.html')

@app.route('/pets')
def show_pets():
    pets = Pet.query.all()
    return render_template('show_pets.html', pets=pets)





@app.route('/new', methods=['GET', 'POST'])
def add_pets():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data, species = form.species.data, photo_url = form.photo_url.data, age = form.age.data, notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect('/pets')
    else:
        return render_template('new.html', form=form)    




@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pets(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/pets')
    else:    
        return render_template('edit.html', form = form, pet=pet)



