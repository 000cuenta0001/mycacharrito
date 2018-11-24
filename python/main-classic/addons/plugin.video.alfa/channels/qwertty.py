# -*- coding: utf-8 -*-
#------------------------------------------------------------
import urlparse,urllib2,urllib,re
import os, sys
from core import jsontools as json
from core import scrapertools
from core import servertools
from core.item import Item
from platformcode import config, logger
from core import httptools
from core import tmdb

host = 'http://qwertty.net'

def mainlist(item):
    logger.info()
    itemlist = []
    itemlist.append( Item(channel=item.channel, title="Recientes" , action="peliculas", url=host))
    itemlist.append( Item(channel=item.channel, title="Mas Vistas" , action="peliculas", url=host + "/?filter=most-viewed"))
    itemlist.append( Item(channel=item.channel, title="Mas popular" , action="peliculas", url=host + "/?filter=popular"))
    itemlist.append( Item(channel=item.channel, title="Mejor valoradas" , action="peliculas", url=host + "/?filter=random"))
    itemlist.append( Item(channel=item.channel, title="Buscar", action="search"))
    return itemlist


def search(item, texto):
    logger.info()
    texto = texto.replace(" ", "+")
    item.url = host + "/?s=%s" % texto
    try:
        return peliculas(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []


def categorias(item):
    logger.info()
    itemlist = []
    data = httptools.downloadpage(item.url).data
    patron  = '<li><a href="([^<]+)">(.*?)</a></li>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)
    for scrapedurl,scrapedtitle in matches:
        scrapedplot = ""
        scrapedthumbnail = ""
        scrapedurl = host + scrapedurl
        itemlist.append( Item(channel=item.channel, action="peliculas", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
    return itemlist


def peliculas(item):
    logger.info()
    itemlist = []
    data = httptools.downloadpage(item.url).data
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>", "", data)
    patron  = '<article id="post-\d+".*?<a href="([^"]+)" title="([^"]+)">.*?<img data-src="(.*?)".*?<span class="duration"><i class="fa fa-clock-o"></i>([^<]+)</span>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)
    for scrapedurl,scrapedtitle,scrapedthumbnail,duracion in matches:
        scrapedplot = ""
        title = "[COLOR yellow]" + duracion + "[/COLOR] " + scrapedtitle
        itemlist.append( Item(channel=item.channel, action="play", title=title , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
    next_page_url = scrapertools.find_single_match(data,'<li><a href="([^"]+)">Next</a>')
    if next_page_url=="":
        next_page_url = scrapertools.find_single_match(data,'<li><a class="current">.*?<li><a href=\'([^\']+)\' class="inactive">')
    
    if next_page_url!="":
        next_page_url = urlparse.urljoin(item.url,next_page_url)
        itemlist.append( Item(channel=item.channel , action="peliculas" , title="Página Siguiente >>" , text_color="blue", url=next_page_url , folder=True) )
    return itemlist


def play(item):
    logger.info()
    itemlist = []
    data = scrapertools.cachePage(item.url)
    pornhub = scrapertools.find_single_match(data,'<iframe src="([^"]+)"')
    data = scrapertools.cachePage(pornhub)
    patron  = '"videoUrl":"(.*?)"'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl in matches:
        scrapedurl = scrapedurl.replace("\/", "/")
        itemlist.append(Item(channel=item.channel, action="play", title=item.title, fulltitle=item.fulltitle, url=scrapedurl,
                            thumbnail=item.thumbnail, plot=item.plot, show=item.title, server="directo", folder=False))
    return itemlist