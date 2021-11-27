from PIL import Image
import json

FILENAME = ''
im_main = Image.open(FILENAME, 'r')
im = im_main.convert('RGB')
width, height = im.size
pixels = list(im.getdata())

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

for i in range(len(pixels)):
	pixels[i] = rgb_to_hex(pixels[i])

file = open('package.json', 'w')
file.write(json.dumps({
    'width': width,
    'height': height,
    'imageData': pixels
}))
file.close()

