from PIL import Image, ImageFilter

imagem = Image.open('soul.jpg')
nova_imagem = imagem.filter(ImageFilter.CONTOUR)
imagem.show()
nova_imagem.show()