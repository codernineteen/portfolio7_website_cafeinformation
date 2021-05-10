from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from forms import AddForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DOWNLOAD_FOLDER'] = '/home/yc6936/mysite/files'
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    map_url = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.String(100), nullable=False)
    coffee_price = db.Column(db.String(100), nullable=False)

db.create_all()


@app.route('/')
def get_all_cafes():
    cafes = Cafe.query.all()
    return render_template('index.html', all_cafes=cafes)

@app.route('/cafe/<int:cafe_id>', methods=["GET","POST"])
def cafe_detail(cafe_id):
    requested_post = Cafe.query.get(cafe_id)
    return render_template('post.html', cafe=requested_post)

@app.route('/add', methods=["GET","POST"])
def add_new_cafe():
    form = AddForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name = form.name.data,
            map_url = form.name.data,
            img_url = form.name.data,
            location = form.name.data,
            has_sockets = form.name.data,
            has_toilet = form.name.data,
            has_wifi = form.name.data,
            can_take_calls = form.name.data,
            seats = form.name.data,
            coffee_price = form.name.data
            )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("get_all_cafes"))
    return render_template('add.html', form=form)

