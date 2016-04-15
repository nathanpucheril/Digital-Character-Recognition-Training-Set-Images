import os
import string
from PIL import Image, ImageOps, ImageFont, ImageDraw

LETTERS = list(string.ascii_uppercase)

def mkdir_safe(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def createTrainingSet(directory = None, val = 0):

    count = 0
    for f in os.listdir("Fonts/"):
        if f == ".DS_Store":
            continue
        # print(f)
        count += 1
        font = ImageFont.truetype("Fonts/"+f,120)
        img = Image.new("RGB", (150,150),(255,255,255))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0),str(val),(0,0,0), font=font)
        draw = ImageDraw.Draw(img)
        img.save(directory + str(val) + "_" + f + ".jpg")


def createLetters():
    for letter in LETTERS:
        mkdir_safe(letter)
        directory = letter + "/"
        createTrainingSet(directory, letter)

def createNumbers():
    for i in range(10):
        mkdir_safe(letter)
        directory = str(i) + "/"
        createTrainingSet(directory, i)
