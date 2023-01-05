import random
import svgwrite

# Set the dimensions of the image
width = 500
height = 500

# Create a new SVG image with the full profile
dwg = svgwrite.Drawing('streets.svg', profile='full')

# Set the pen color and width
dwg.add(dwg.style('.line{stroke: black; stroke-width: 1;}'))

# Generate a random number of streets
num_streets = random.randint(10, 20)

# Set the seed value for the random number generator
random.seed(12345)

# Draw the streets
for i in range(num_streets):
    # Generate random start and end points for the street
    if random.randint(0, 1) == 0:
        # Draw a vertical street
        x1 = random.randint(0, width)
        x2 = x1
        y1 = 0
        y2 = height
    else:
        # Draw a horizontal street
        y1 = random.randint(0, height)
        y2 = y1
        x1 = 0
        x2 = width

    # Draw the street
    dwg.add(dwg.line((x1, y1), (x2, y2), stroke='black', class_='line'))

# Save the SVG image
dwg.save()
