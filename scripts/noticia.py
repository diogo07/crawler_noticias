
class Noticia:

    def __init__(self, titulo, descricao, conteudo, data, link, url_image):
        self.titulo = titulo
        self.descricao = descricao
        self.conteudo = conteudo
        self.data = data
        self.link = link
        self.url_image = url_image


    def __repr__(self):
        return str(self.__dict__)