# main.py
import json
import random
from datetime import datetime

def generate_fake_multipliers():
    return [round(random.uniform(1.0, 5.0), 2) for _ in range(30)]

data = {
    "timestamp": datetime.utcnow().isoformat(),
    "multipliers": generate_fake_multipliers()
}

with open("results.json", "w") as f:
    json.dump(data, f, indent=2)

print("Multipliers updated!")
