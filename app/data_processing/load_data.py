from app.models import ClimateData, db
import pandas as pd
from datetime import datetime
import random

def load_initial_data():
    if ClimateData.query.count() == 0:
        print("Loading initial climate data...")
        
        # Generate synthetic data
        countries = ['USA', 'UK', 'Japan', 'Germany', 'Brazil', 'Australia']
        cities = {
            'USA': ['New York', 'Los Angeles', 'Chicago'],
            'UK': ['London', 'Manchester', 'Edinburgh'],
            'Japan': ['Tokyo', 'Osaka', 'Kyoto'],
            'Germany': ['Berlin', 'Munich', 'Hamburg'],
            'Brazil': ['Rio de Janeiro', 'São Paulo', 'Brasília'],
            'Australia': ['Sydney', 'Melbourne', 'Brisbane']
        }
        
        records = []
        for year in range(1990, 2023):
            for month in range(1, 13):
                date = datetime(year, month, 15)
                for country in countries:
                    for city in cities[country]:
                        base_temp = {
                            'USA': 10,
                            'UK': 8,
                            'Japan': 12,
                            'Germany': 9,
                            'Brazil': 25,
                            'Australia': 20
                        }[country]
                        
                        temp_variation = random.uniform(-5, 5)
                        precipitation = random.uniform(0, 100)
                        humidity = random.uniform(30, 90)
                        
                        records.append({
                            'country': country,
                            'city': city,
                            'date': date,
                            'temperature': round(base_temp + temp_variation, 1),
                            'precipitation': round(precipitation, 1),
                            'humidity': round(humidity, 1)
                        })
        
        # Bulk insert
        for record in records:
            climate_data = ClimateData(**record)
            db.session.add(climate_data)
        
        db.session.commit()
        print(f"Loaded {len(records)} climate data records")