import sys

# Variant 1
"""
amount = float(sys.argv[1])
result = amount / 1.24

print("Summa ilma km-ta on", round(result, 2))
"""

# Variant 2
print("Summa ilma km-ta on", round(float(sys.argv[1]) / 1.24, 2))
