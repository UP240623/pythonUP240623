import random
import string
def list_hexa():                                                                        #1
    hexa_col = ['#' + ''.join(random.choices(string.hexdigits, k=6))]
    return hexa_col
print(list_hexa())

def list_rgb():                                                                         #2
    rgb_col = [(random.randint(0,255), random.randint(0,255), random.randint(0,255))]
    return rgb_col
print(list_rgb())

type_col=input("Hexa or RGB: ")                                                         #3
num= int(input("Amount of colors: "))
if type_col == "Hexa" or "hexa" or "HEXA":
    def generate_colors():
        hexa_colors = ['#' + ''.join(random.choices(string.hexdigits, k=6)) for _ in range(num)]
        return hexa_colors
    print(generate_colors())
elif type_col == "RGB" or "rgb" or "Rgb":
    def generate_colors():
        rgb_colors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(num)]
        return rgb_colors
    print(generate_colors())