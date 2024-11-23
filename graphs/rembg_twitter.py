from rembg import remove
from PIL import Image
input_path = 'graphs/20230620_091912.jpg'
# input_path = 'graphs/6_5x9_2_1.png'
# input_path = 'graphs/6x9_c.png'
inp = Image.open(input_path)
inp.show()

output_path = 'output_.png'
output = remove(inp)
output.show()
output.save(output_path)