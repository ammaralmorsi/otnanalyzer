import random

# Generate 64 random decimal numbers
decimal_row = [random.randint(0, 255) for _ in range(64)]

# Convert the list to a single string with spaces
decimal_string = ' '.join(map(str, decimal_row))

print(decimal_string)
