from rembg import remove
from PIL import Image
input_path = 'graphs/20230620_091912.jpg'
output_path = '20230620_091912.png'
inp = Image.open(input_path)
inp.show()
# display(inp)
output = remove(inp)
output.show()
output.save = (output_path)
# Image.open(output_path)
# Image.open('620230620_091912__.jpg')