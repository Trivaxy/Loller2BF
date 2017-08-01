from PIL import Image
from os import path, chmod
from sys import exit
# load image, read it pixel by pixel, and give an output text file with brainf*ck code.
bfCode = ""
try:
    image = Image.open(path.dirname(path.realpath(__file__)) + "\Input.jpg").convert("RGB")
except:
    print "No Input image file found. Make sure to supply one with that name in the same directory as the .exe"
    raw_input("")
    exit()

pixels = image.load()
dimensions = image.size

x = 0
y = 0

for x in range(0, dimensions[0]):
    for y in range(0, dimensions[1]):
        if pixels[x, y] == (255, 0, 0):
            bfCode += ">"
        elif pixels[x, y] == (128, 0, 0):
            bfCode += "<"
        elif pixels[x, y] == (0, 255, 0):
            bfCode += "+"
        elif pixels[x, y] == (0, 128, 0):
            bfCode += "-"
        elif pixels[x, y] == (0, 0, 255):
            bfCode += "."
        elif pixels[x, y] == (0, 0, 128):
            bfCode += ","
        elif pixels[x, y] == (255, 255, 0):
            bfCode += "["
        elif pixels[x, y] == (128, 128, 0):
            bfCode += "]"

print bfCode
if raw_input("Write the BF code into a text file? (y / n)\n").lower() == "y":
    file = open('Out.txt', 'w')
    file.write(bfCode)
    file.close()
