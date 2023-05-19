from pathlib import Path

path = Path("ecommerce")
for file in path.glob("*.py"):
    print(file)
