from datetime import datetime
from app import db

class ClimateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), index=True)
    city = db.Column(db.String(100), index=True)
    date = db.Column(db.Date, index=True)
    temperature = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    humidity = db.Column(db.Float)
    
    def __repr__(self):
        return f'<ClimateData {self.country}, {self.city}, {self.date}>'

class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(20), default='light')
    default_view = db.Column(db.String(50), default='temperature')
    
    def __repr__(self):
        return f'<UserSettings {self.id}>'