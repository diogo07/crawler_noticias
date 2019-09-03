from scripts.crawler import get_html
from scripts.scraping import get_noticias
from scripts.database import insert_noticias

html = get_html('https://g1.globo.com/economia/tecnologia/')
noticias = get_noticias(html)
insert_noticias(noticias)