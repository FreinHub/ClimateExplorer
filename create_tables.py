from app import create_app, db

app = create_app()
print(f"DB path: {app.config['SQLALCHEMY_DATABASE_URI']}")

with app.app_context():
    db.create_all()
    print("Таблицы успешно созданы в:", app.config['SQLALCHEMY_DATABASE_URI'])