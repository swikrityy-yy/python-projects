# Image Filter: Grayscale and Sepia

## Description
This Python program applies **grayscale** and **sepia** filters to an image using pixel manipulation.  
- **Grayscale** converts a color image to shades of gray.  
- **Sepia** adds a warm, vintage tone to the image.  

The program uses the `images` module to load, manipulate, and display images.

---

## Features
- Load any image supported by the `images` module.
- View the **original image**, **grayscale version**, and **sepia version** sequentially.
- Understand how pixel RGB values are manipulated to achieve image effects.

---

## Requirements
- Python 3.x
- `images` module (used for loading and displaying images)

---

## How to Run
1. Clone this repository:  
   ```bash
   git clone <your-repo-url>
 Image Filter: Grayscale and Sepia

## Description
This Python program applies **grayscale** and **sepia** filters to an image using pixel manipulation.  
- **Grayscale** converts a color image to shades of gray.  
- **Sepia** adds a warm, vintage tone to the image.  

The program uses the `images` module to load, manipulate, and display images.

---

## Features
- Load any image supported by the `images` module.
- View the **original image**, **grayscale version**, and **sepia version** sequentially.
- Understand how pixel RGB values are manipulated to achieve image effects.

---

## Requirements
- Python 3.x
- `images` module (used for loading and displaying images)

---

## How to Run
1. Clone this repository:  
   ```bash
   git clone <your-repo-url>

   
Navigate to the folder:

cd <your-repo-folder>
Run the program:


python sepia.py
Enter the filename of your image when prompted.

Close each displayed image window to move to the next filter.

How it Works
Grayscale filter:
Each pixel's RGB values are converted to brightness using the formula:


lum = 0.299*R + 0.587*G + 0.114*B
The pixel is then set to (lum, lum, lum).

Sepia filter:
Grayscale pixels are adjusted:

Dark pixels → slightly increase red, decrease blue

Mid-range → moderately increase red, decrease blue

Bright → slightly boost red, slightly dim blue
This creates a warm, vintage tone while keeping green balanced.

Author
Swikriti 
