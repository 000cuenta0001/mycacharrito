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
from core import jsontools

host = 'http://mporno.tv'

def mainlist(item):
    logger.info()
    itemlist = []
    itemlist.append( Item(channel=item.channel, title="Novedades" , action="peliculas", url=host + "/most-recent/", plot="/most-recent/"))
    itemlist.append( Item(channel=item.channel, title="Mejor valoradas" , action="peliculas", url=host + "/top-rated/", plot="/top-rated/"))
    itemlist.append( Item(channel=item.channel, title="Mas vistas" , action="peliculas", url=host + "/most-viewed/", plot="/most-viewed/"))
    itemlist.append( Item(channel=item.channel, title="Longitud" , action="peliculas", url=host + "/longest/", plot="/longest/"))
    itemlist.append( Item(channel=item.channel, title="Categorias" , action="categorias", url=host + "/channels/"))
    itemlist.append( Item(channel=item.channel, title="Buscar", action="search"))
    return itemlist


def search(item, texto):
    logger.info()
    texto = texto.replace(" ", "+")
    item.url = host + "/search/videos/%s/page1.html" % texto
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
    patron  = '<h3><a href="([^"]+)">(.*?)</a> <small>(.*?)</small></h3>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    scrapertools.printMatches(matches)
    for scrapedurl,scrapedtitle,cantidad in matches:
        scrapedplot = scrapedurl.replace("http://mporno.unblckd.org/", "").replace("page1.html", "")
        scrapedthumbnail = ""
        scrapedtitle = scrapedtitle + "  " + cantidad
        itemlist.append( Item(channel=item.channel, action="peliculas", title=scrapedtitle , url=scrapedurl , thumbnail=scrapedthumbnail , plot=scrapedplot , folder=True) )
    return itemlist


def peliculas(item):
    logger.info()
    itemlist = []
    data = httptools.downloadpage(item.url).data
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>", "", data)
	

	
    patron  = '<img class="content_image" src="([^"]+).mp4/.*?" alt="([^"]+)".*?this.src="(.*?)"'
    matches = re.compile(patron,re.DOTALL).findall(data)
    for scrapedurl,scrapedtitle,scrapedthumbnail in matches:
        contentTitle = scrapedtitle
        title = scrapedtitle
        scrapedurl = scrapedurl.replace("/thumbs/", "/videos/") + ".mp4"
        thumbnail = scrapedthumbnail
        plot = item.plot
        year = ""
        itemlist.append( Item(channel=item.channel, action="play" , title=title , url=scrapedurl, thumbnail=thumbnail, plot=plot, contentTitle=contentTitle, infoLabels={'year':year} ))
    next_page_url = scrapertools.find_single_match(data,'<a href=\'([^\']+)\' class="next">Next &gt;&gt;</a>')
    if next_page_url!="":
        next_page_url = urlparse.urljoin(item.url,next_page_url)
        itemlist.append( Item(channel=item.channel , action="peliculas" , title="Página Siguiente >>" , text_color="blue", url=next_page_url , folder=True) )
        

    # else:
        # patron  = '<a href=\'([^\']+)\' class="next">Next &gt;&gt;</a>'
        # next_page = re.compile(patron,re.DOTALL).findall(data)
        # next_page = scrapertools.find_single_match(data,'class="last" title=.*?<a href="([^"]+)">')
        # plot = item.plot
        # next_page =  next_page[0]
        # next_page = host + plot + next_page
        # itemlist.append( Item(channel=item.channel, action="peliculas", title=next_page , text_color="blue", url=next_page, plot=plot ) )
    return itemlist

