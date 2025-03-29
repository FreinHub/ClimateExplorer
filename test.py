import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
sys.path.append(str(Path(__file__).parent))

try:
    from app import create_app
    print("✅ Успешный импорт create_app!")
    app = create_app()
    print("✅ Приложение создано успешно!")
except Exception as e:
    print(f"❌ Ошибка: {e}")
    raise