from PIL import Image, ImageFilter


img = Image.open('IMG_0013.JPG')
# 应用模糊滤镜
# blurred_img = img.filter(ImageFilter.BLUR)
# blurred_img.show()

# 应用锐化滤镜
sharpened_img = img.filter(ImageFilter.SHARPEN)
sharpened_img.show()
