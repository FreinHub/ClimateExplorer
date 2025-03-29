from app.data_processing.visualizations import generate_visualizations, generate_additional_visualizations
from datetime import datetime

# Сначала объявляем тестовые данные
test_data = [
    {
        'date': datetime(2023, 1, 1),
        'temperature': 15.2,
        'precipitation': 32.1,
        'humidity': 65,
        'country': 'TestCountry',
        'city': 'TestCity'
    },
    {
        'date': datetime(2023, 1, 2),
        'temperature': 16.8,
        'precipitation': 28.4,
        'humidity': 62,
        'country': 'TestCountry',
        'city': 'TestCity'
    }
]

# Теперь можем использовать test_data
print("=== Тестируем generate_visualizations ===")
print("Первый элемент данных:", test_data[0])  # Печатаем образец данных

try:
    plots = generate_visualizations(test_data, 'TestCountry')
    print("✅ Успех! Созданы графики:", list(plots.keys()))
except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\n=== Тестируем generate_additional_visualizations ===")
try:
    additional_plots = generate_additional_visualizations(test_data)
    print("✅ Успех! Дополнительные графики:", list(additional_plots.keys()))
except Exception as e:
    print(f"❌ Ошибка: {e}")