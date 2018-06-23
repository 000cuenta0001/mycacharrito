# -*- coding: utf-8 -*-

import re
import urlparse

from core import httptools
from core import scrapertools
from core import servertools
from core import tmdb
from core.item import Item
from platformcode import config, logger
from channelselector import get_thumb

host = 'http://verhdpelis.com/'
headers = [['User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'],
           ['Referer', host]]

global duplicado
global itemlist
global temp_list
canal = 'cinefoxtv'

tgenero = {"Comedia": "https://s7.postimg.cc/ne9g9zgwb/comedia.png",
           "Suspenso": "https://s13.postimg.cc/wmw6vl1cn/suspenso.png",
           "Drama": "https://s16.postimg.cc/94sia332d/drama.png",
           "Acción": "https://s3.postimg.cc/y6o9puflv/accion.png",
           "Aventuras": "https://s10.postimg.cc/6su40czih/aventura.png",
           "Animacion": "https://s13.postimg.cc/5on877l87/animacion.png",
           "Ciencia Ficcion": "https://s9.postimg.cc/diu70s7j3/cienciaficcion.png",
           "Terror": "https://s7.postimg.cc/yi0gij3gb/terror.png",
           "Documentales": "https://s16.postimg.cc/7xjj4bmol/documental.png",
           "Musical": "https://s29.postimg.cc/bbxmdh9c7/musical.png",
           "Western": "https://s23.postimg.cc/lzyfbjzhn/western.png",
           "Belico": "https://s23.postimg.cc/71itp9hcr/belica.png",
           "Crimen": "https://s4.postimg.cc/6z27zhirx/crimen.png",
           "Biográfica": "https://s15.postimg.cc/5lrpbx323/biografia.png",
           "Deporte": "https://s13.postimg.cc/xuxf5h06v/deporte.png",
           "Fantástico": "https://s10.postimg.cc/pbkbs6j55/fantastico.png",
           "Estrenos": "https://s21.postimg.cc/fy69wzm93/estrenos.png",
           "Película 18+": "https://s15.postimg.cc/exz7kysjf/erotica.png",
           "Thriller": "https://s22.postimg.cc/5y9g0jsu9/thriller.png",
           "Familiar": "https://s7.postimg.cc/6s7vdhqrf/familiar.png",
           "Romanticas": "https://s21.postimg.cc/xfsj7ua0n/romantica.png",
           "Intriga": "https://s27.postimg.cc/v9og43u2b/intriga.png",
           "Infantil": "https://s23.postimg.cc/g5rmazozv/infantil.png"}


def mainlist(item):
    logger.info()

    itemlist = []

    itemlist.append(item.clone(title="Todas", action="lista", thumbnail=get_thumb('all', auto=True),
                               fanart='https://s18.postimg.cc/fwvaeo6qh/todas.png', extra='peliculas/',
                               url=host + 'page/1.html'))

    itemlist.append(
        itemlist[-1].clone(title="Generos", action="generos", thumbnail=get_thumb('genres', auto=True),
                           fanart='https://s3.postimg.cc/5s9jg2wtf/generos.png', url=host))

    itemlist.append(
        itemlist[-1].clone(title="Mas Vistas", action="lista", thumbnail=get_thumb('more watched', auto=True),
                           fanart='https://s9.postimg.cc/wmhzu9d7z/vistas.png',
                           url=host + 'top-peliculas-online/1.html'))

    itemlist.append(itemlist[-1].clone(title="Buscar", action="search", thumbnail=get_thumb('search', auto=True),
                                       fanart='https://s30.postimg.cc/pei7txpa9/buscar.png', url=host + 'search/'))

    return itemlist


def lista(item):
    logger.info()
    itemlist = []
    duplicado = []
    max_items = 24
    next_page_url = ''

    data = httptools.downloadpage(item.url).data
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>", "", data)
    data = scrapertools.decodeHtmlentities(data)
    patron = '"box_image_b.*?"><a href="([^"]+)" title=".*?><img src="([^"]+)" alt="(.*?)(\d{4}).*?"'
    matches = re.compile(patron, re.DOTALL).findall(data)

    if item.next_page != 'b':
        if len(matches) > max_items:
            next_page_url = item.url
            matches = matches[:max_items]
            next_page = 'b'
    else:
        matches = matches[max_items:]
        next_page = 'a'
        patron_next_page = '<a class="page dark gradient" href="([^"]+)">PROXIMO'
        matches_next_page = re.compile(patron_next_page, re.DOTALL).findall(data)
        if len(matches_next_page) > 0:
            next_page_url = urlparse.urljoin(item.url, matches_next_page[0])

    for scrapedurl, scrapedthumbnail, scrapedtitle, scrapedyear in matches:

        url = scrapedurl
        thumbnail = scrapedthumbnail
        contentTitle = re.sub(r"\(.*?\)|\/.*?|\(|\)|.*?\/|&excl;", "", scrapedtitle)
        title = scrapertools.decodeHtmlentities(contentTitle) + '(' + scrapedyear + ')'
        fanart = ''
        plot = ''

        if url not in duplicado:
            itemlist.append(
                Item(channel=item.channel, action='findvideos', title=title, url=url, thumbnail=thumbnail, plot=plot,
                     fanart=fanart, contentTitle=contentTitle, infoLabels={'year': scrapedyear}))
            duplicado.append(url)

    tmdb.set_infoLabels_itemlist(itemlist, seekTmdb=True)
    if next_page_url != '':
        itemlist.append(Item(channel=item.channel, action="lista", title='Siguiente >>>', url=next_page_url,
                             thumbnail='https://s16.postimg.cc/9okdu7hhx/siguiente.png', extra=item.extra,
                             next_page=next_page))
    return itemlist


def generos(item):
    logger.info()

    itemlist = []

    data = httptools.downloadpage(item.url).data
    patron = '<li><a href="([^"]+)"><i class="fa fa-caret-right"><\/i> <strong>Películas de (.*?)<\/strong><\/a><\/li>'
    matches = re.compile(patron, re.DOTALL).findall(data)

    for scrapedurl, scrapedtitle in matches:
        url = scrapedurl
        if scrapedtitle in tgenero:
            thumbnail = tgenero[scrapedtitle]
        else:
            thumbnail = ''
        title = scrapedtitle
        fanart = ''
        plot = ''

        if title != 'Series':
            itemlist.append(
                Item(channel=item.channel, action='lista', title=title, url=url, thumbnail=thumbnail, plot=plot,
                     fanart=fanart))
    return itemlist


def getinfo(page_url):
    logger.info()
    data = httptools.downloadpage(page_url).data
    plot = scrapertools.find_single_match(data, '<\/em>\.(?:\s*|.)(.*?)\s*<\/p>')
    info = plot

    return info


def findvideos(item):
    logger.info()
    itemlist = []
    info = getinfo(item.url)
    data = httptools.downloadpage(item.url, headers=headers).data
    patron = 'src="(.*?)" style="border:none;'
    matches = re.compile(patron, re.DOTALL).findall(data)
    for scrapedurl in matches:
        itemlist.extend(servertools.find_video_items(data=scrapedurl))

    for videoitem in itemlist:
        videoitem.title = item.contentTitle
        videoitem.channel = item.channel
        videoitem.plot = info
        videoitem.action = "play"
        videoitem.folder = False
        videoitem.infoLabels=item.infoLabels

    if config.get_videolibrary_support() and len(itemlist) > 0 and item.extra != 'findvideos':
        itemlist.append(
            Item(channel=item.channel, title='[COLOR yellow]Añadir esta pelicula a la videoteca[/COLOR]', url=item.url,
                 action="add_pelicula_to_library", extra="findvideos", contentTitle=item.contentTitle))

    return itemlist


def search(item, texto):
    logger.info()
    texto = texto.replace(" ", "-")
    item.url = item.url + texto
    if texto != '':
        return lista(item)


def newest(categoria):
    logger.info()
    itemlist = []
    item = Item()
    # categoria='peliculas'
    try:
        if categoria in ['peliculas','latino']:
            item.url = host + 'page/1.html'
        elif categoria == 'infantiles':
            item.url = host + 'peliculas-de-genero/infantil/1.html'
        itemlist = lista(item)
        if itemlist[-1].title == 'Siguiente >>>':
            itemlist.pop()
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist
