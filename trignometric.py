import math

def calculate_trigonometric_values(degrees):

# Convert degrees to radians because math functions use radians

    radians = math.radians(degrees)

    print(radians)

# Calculate sine, cosine, and tangent

    sine_value = math.sin(radians)

    cosine_value = math.cos(radians)

    tangent_value = math.tan(radians)

# Print the results

    print(sine_value)

    print(cosine_value)

    print(tangent_value)

# --- Example Usage ---

# Example 1: Standard angle (90 degrees)

calculate_trigonometric_values(90)