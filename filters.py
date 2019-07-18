from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    im = Image.open(filename)
    return im


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im, filename):
    im.save(filename)
    show_img(im)



# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Define color constants to use for recoloring.
  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Return a new Image, with grayscale filter applied.
def grayscale(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Process the pixels in the image.
  for p in pixels:
    new_p = avg_pixel(p)
    new_pixels.append(new_p)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim

# Helper function.
# Return a grayscale tuple for a single pixel value.
def avg_pixel(pixel):
  # Use the average of p's RGB values to set a new pixel value.
  avg = (pixel[0] + pixel[1] + pixel[2]) // 3 # Use // for int division.
  return (avg, avg, avg) # R = G = B will be a gray pixel!
