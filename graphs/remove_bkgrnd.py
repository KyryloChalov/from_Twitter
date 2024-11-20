from rembg import remove
from PIL import Image

input_path = "graphs/20221203_105151.jpg"
# input_path = "20230620_092134.jpg"
output_path = "output.png"

input_pic = Image.open(input_path)
output = remove(input_pic)
output.show()
output.save(output_path)