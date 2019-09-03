from bs4 import BeautifulSoup
from scripts.noticia import Noticia
from scripts.crawler import get_html
from scripts.dados_noticia import DadosNoticia
from scripts.utils import save_image, gerar_code



def get_noticias(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    dados = soup.find_all('div', class_='bastian-feed-item')

    noticias = []

    for dado in dados:
        titulo = dado.find('div', class_='_et').get_text()
        url = dado.find('div', class_='_et').a.get('href')
        descricao = dado.find('div', class_='feed-post-body-resumo').get_text()
        code = gerar_code()
        img = dado.find('picture', class_='bstn-fd-cover-picture')
        save_image(img.img.get('src'), 'image' + code + '.jpg')
        dados_noticia = get_dados_noticia(url)
        noticia = Noticia(titulo, descricao, dados_noticia.conteudo, dados_noticia.data, url, 'image' + code)
        noticias.append(noticia)
    return noticias

def get_dados_noticia(url):
    html = get_html(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    html_conteudo = soup.find('div', class_='protected-content')
    conteudos = html_conteudo.find_all('div', class_='content-text')
    conteudo = ''

    for c in conteudos:
        conteudo = "".join([conteudo, c.get_text()])

    data = soup.find('p', class_='content-publication-data__updated')
    return DadosNoticia(data.time.get('datetime'), conteudo.replace('"', ''))