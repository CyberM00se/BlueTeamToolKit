from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('Images/pc.jpg')
im2 = Image.open('Images/ocean.jpeg')

im1.paste(im2)
im1.save('Images/NewImage1.jpg', quality=95)
