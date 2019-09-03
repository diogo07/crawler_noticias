import random
import urllib.request

def save_image(url, nome):
    uopen = urllib.request.urlopen(url)
    stream = uopen.read()
    file = open('../resource/'+nome, 'wb')
    file.write(stream)
    file.close()

def gerar_code():
    caracteres = '1234567890'
    list_caracteres = list(caracteres)
    random.shuffle(list_caracteres)

    return "".join(list_caracteres)[0:4]