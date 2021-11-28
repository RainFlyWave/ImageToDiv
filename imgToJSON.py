from PIL import Image
import json

FILENAME = ''                           # enter here your picture filename (with extenstion such as .jpg)
im_main = Image.open(FILENAME, 'r')     # open picture
im = im_main.convert('RGB')             # convert picture into RGB
width, height = im.size                 # get the height and width of the image
pixels = list(im.getdata())             # get color for every pixel in the image

def rgb_to_hex(rgb):            # helper function that converts RGB values to HEX values
    """Simple function that takes one arguemnt, RGB color and returns the same value in HEX notation."""
    return '#%02x%02x%02x' % rgb

for i in range(len(pixels)):            # iterate through all the pixels in the image
	pixels[i] = rgb_to_hex(pixels[i])   # convert every one of them ingo HEX notation

file = open('package.json', 'w')        # create package.json file
file.write(json.dumps({                 # parse data and save it to the package.json file
    'width': width,
    'height': height,
    'imageData': pixels
}))
file.close()

