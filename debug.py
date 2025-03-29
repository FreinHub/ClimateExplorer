import sys
print("Python version:", sys.version)
print("Current path:", sys.path)

try:
    from app import create_app
    print("✅ create_app imported successfully!")
except Exception as e:
    print(f"❌ Import failed: {e}")