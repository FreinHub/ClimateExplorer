from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
from app.models import ClimateData
from app.forms import UploadForm, FilterForm
from app.data_processing.visualizations import generate_visualizations, generate_additional_visualizations
from app import db
import pandas as pd
from io import BytesIO
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = FilterForm()
    
    # Get filter parameters
    country = request.args.get('country', 'All')
    year_range = request.args.get('year_range', '1900-2023')
    start_year, end_year = map(int, year_range.split('-'))
    
    # Query data
    query = ClimateData.query.filter(
        ClimateData.date >= datetime(start_year, 1, 1),
        ClimateData.date <= datetime(end_year, 12, 31)
    )
    
    if country != 'All':
        query = query.filter_by(country=country)
    
    data = query.all()
    
    # Generate visualizations
    plots = generate_visualizations(data, country)
    additional_plots = generate_additional_visualizations(data)
    
    return render_template('dashboard.html', 
                        plots=plots,
                        additional_plots=additional_plots,
                        form=form,
                        countries=get_countries(),
                        selected_country=country,
                        year_range=year_range)

@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        try:
            df = pd.read_csv(form.file.data)
            process_uploaded_data(df)
            flash('Data uploaded successfully!', 'success')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            flash(f'Error processing file: {str(e)}', 'danger')
    
    return render_template('upload.html', form=form)

@bp.route('/download_sample')
def download_sample():
    # Generate sample data
    data = {
        'country': ['USA', 'UK', 'Japan'],
        'city': ['New York', 'London', 'Tokyo'],
        'date': ['2020-01-01', '2020-01-01', '2020-01-01'],
        'temperature': [5.2, 3.8, 8.1],
        'precipitation': [45.2, 32.1, 28.7],
        'humidity': [65, 72, 58]
    }
    df = pd.DataFrame(data)
    
    # Create CSV in memory
    output = BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name='climate_data_sample.csv'
    )

def get_countries():
    countries = ClimateData.query.with_entities(
        ClimateData.country
    ).distinct().all()
    return [c[0] for c in countries]

def process_uploaded_data(df):
    # Process and validate the uploaded data
    required_columns = ['country', 'city', 'date', 'temperature', 'precipitation']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns")
    
    # Convert and save to database
    for _, row in df.iterrows():
        record = ClimateData(
            country=row['country'],
            city=row['city'],
            date=datetime.strptime(row['date'], '%Y-%m-%d'),
            temperature=row['temperature'],
            precipitation=row['precipitation'],
            humidity=row.get('humidity', None)
        )
        db.session.add(record)
    
    db.session.commit()