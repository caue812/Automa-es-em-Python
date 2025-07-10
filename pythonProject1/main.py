from PIL import Image

def modificar_pixel(pixel: tuple, percentual:float) -> tuple:
    r,g,b = pixel
    escala = 1+percentual/100
    r,g,b = int(r * escala), int(g * escala), int(b * escala)
    return min(r,255), min(g,255), min(b,255)

imagem = Image.open('soul.jpg')
imagem.show()
# imagem = imagem.resize((20,20))
pixels = imagem.getdata()
nova_imagem = []
for pixel in pixels:
    nova_imagem.append(modificar_pixel(pixel, 50))
imagem.putdata(nova_imagem)
imagem.show()





#imagem = imagem.convert('L')
# imagem = imagem.rotate(45,fillcolor=(255,0,0))
# imagem = imagem.resize((50,50))
# imagem.save('convertida.png')
# imagem.show() # exibir imagem
#
# print(imagem.format)
# print(imagem.size)
# print(imagem.mode)
