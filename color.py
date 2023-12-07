from PIL import Image
import sys 

def generate_colored_image(name, color_code, width=500, height=500):
    # Create a new image with the specified size and color
    image = Image.new("RGB", (width, height), color_code)

    # Save the image to a file (optional)
    image.save(name+".png")

    # Display the image (optional)
    image.show()

# Example: Generate a red image (color code for red: (255, 0, 0))
if __name__ == "__main__":
    # Check if three command line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py R G B name")
        sys.exit(1)

    # Extract RGB values from command line arguments
    try:
        r = int(sys.argv[1])
        g = int(sys.argv[2])
        b = int(sys.argv[3])
        name = sys.argv[4] + ""
    except ValueError:
        print("Error: RGB values must be integers.")
        sys.exit(1)

    # Generate the colored image
    generate_colored_image(name, (r, g, b))
