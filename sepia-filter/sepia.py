from images import Image

def greyscale(image):
    """
    Converts a color image to grayscale by adjusting each pixel's
    red, green, and blue values to match its luminance.
    """
    # Loop through every pixel in the image
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            # Get the current pixel's RGB values
            (r, g, b) = image.getPixel(x, y)

            # Calculate brightness/luminance using the standard formula
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b  # total brightness

            # Set the pixel to grayscale (all channels have same value)
            image.setPixel(x, y, (lum, lum, lum))


def sepia(image):
    """
    Applies a sepia tone effect to an image (warm, old-timey look).
    Assumes the image is already in grayscale.
    """
    # Loop through each pixel
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            # Get the current pixel's RGB values
            (red, green, blue) = image.getPixel(x, y)

            # Apply sepia adjustments based on brightness
            if red < 63:
                # Dark pixels: slightly increase red, decrease blue
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                # Mid-range pixels: moderately increase red, decrease blue
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                # Bright pixels: slightly boost red, slightly dim blue
                red = min(int(red * 1.08), 255)  # cap at 255
                blue = int(blue * 0.93)

            # Green channel stays the same for balance
            image.setPixel(x, y, (red, green, blue))


def main():
    """
    Main function to run the program:
    - Loads an image
    - Displays the original image
    - Converts it to grayscale and displays
    - Applies sepia effect and displays
    """
    # Prompt user for image filename
    filename = input('Enter the file name: ')
    
    # Load image object
    image = Image(filename)

    # Show original image
    print("Showing the original image. Close it to continue.")
    image.draw()

    # Convert to grayscale
    greyscale(image)
    print("Showing the grayscale image. Close it to continue.")
    image.draw()

    # Apply sepia tone
    sepia(image)
    print("Showing the sepia-toned image. Close it to finish.")
    image.draw()


# Run the program
if __name__ == "__main__":
    main()
