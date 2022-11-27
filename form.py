
from flask_wtf import FlaskForm #dependencia instalada
from wtforms import StringField,SubmitField # variaveis  strings de campo do form

from wtforms.validators import DataRequired

class NameForm(FlaskForm):
 name=StringField('Qual é os eu nome ',validators=[DataRequired()])
 submit=SubmitField('submit')
