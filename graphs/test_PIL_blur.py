from PIL import Image, ImageFilter

original = Image.open("graphs/20221203_105151.jpg")  # завантажити зображення з жорсткого диску
blurred = original.filter(ImageFilter.BLUR)  # розмити зображення

original.show()  # показати обидва зображення
blurred.show()
