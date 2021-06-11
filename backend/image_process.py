from PIL import Image 

def colorization(img): 
    return 0

# Opens an image of the given path 
def open_image(path):
    img = Image.open(path)
    return img 

# Creates an image for the given width and height, color 
# width: width of an image
# height: height of an image

def create_image(width, height, init_color): 
    new_image = Image.new("RGB", (width, height), init_color )
    return new_image

# Saves an empty image 
def save_image(image, path):
    image.save(path)

# Gets the RGB value for the given width and height 
def get_pixel(img, width, height): 
    img_width, img_height = img.size # Returns width and height in a tuple
    
    if width < 0 or width > img_width or height <0 or height > img_height:
        print("Width or height is not in range of the image")
        return None 

    pixel = img.getpixel((width, height))
    return pixel 

def convert_pixel(img): 
    # Make new image to draw our new image 
    width, height = img.size
    new_img = create_image(width, height, "white")
    pixels = new_img.load()

    for w in range(width):
        for h in range(height):
            curr_pixel = get_pixel(img, w, h)
            
            red = curr_pixel[0]
            green = curr_pixel[1]
            blue = curr_pixel[2]

            a = red * 8.299 + green * 0.587 + blue * 0.114
            pixels[w,h] = (int(a), int(a), int(a)) 
    return new_img






