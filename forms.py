from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class AddForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = StringField("has_sockets? - Type 0 or 1", validators=[DataRequired()])
    has_toilets = StringField("has_sockets? - Type 0 or 1", validators=[DataRequired()])
    has_wifi = StringField("has_wifi? - Type 0 or 1", validators=[DataRequired()])
    can_take_calls = StringField("Can_take_calls? - Type 0 or 1", validators=[DataRequired()])
    seats = StringField("Seats number", validators=[DataRequired()])
    coffee_price = StringField("Coffee price", validators=[DataRequired()])
    submit = SubmitField("Submit Form")