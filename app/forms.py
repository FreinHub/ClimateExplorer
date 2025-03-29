from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(FlaskForm):
    file = FileField('Climate Data CSV', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'CSV files only!')
    ])
    submit = SubmitField('Upload')

class FilterForm(FlaskForm):
    country = SelectField('Country', choices=[])
    year_range = SelectField('Year Range', choices=[
        ('1900-2023', 'All Years'),
        ('2010-2023', 'Recent (2010-2023)'),
        ('2000-2009', '2000s'),
        ('1990-1999', '1990s')
    ])
    submit = SubmitField('Apply Filters')