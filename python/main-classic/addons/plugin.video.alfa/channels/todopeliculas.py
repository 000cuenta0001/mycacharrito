# -*- coding: utf-8 -*-

import re
import sys
import urllib
import urlparse
import time

from channelselector import get_thumb
from core import httptools
from core import scrapertools
from core import servertools
from core.item import Item
from platformcode import config, logger
from core import tmdb
from lib import generictools
from channels import filtertools
from channels import autoplay


#IDIOMAS = {'CAST': 'Castellano', 'LAT': 'Latino', 'VO': 'Version Original'}
IDIOMAS = {'Castellano': 'CAST', 'Latino': 'LAT', 'Version Original': 'VO'}
list_language = IDIOMAS.values()
list_quality = []
list_servers = ['torrent']

host = 'http://www.todo-peliculas.com/'
channel = "todopeliculas"

categoria = channel.capitalize()
__modo_grafico__ = config.get_setting('modo_grafico', channel)
timeout = config.get_setting('timeout_downloadpage', channel)


def mainlist(item):
    logger.info()
    itemlist = []
    
    thumb_cartelera = get_thumb("now_playing.png")
    thumb_pelis = get_thumb("channels_movie.png")
    thumb_pelis_hd = get_thumb("channels_movie_hd.png")
    thumb_buscar = get_thumb("search.png")
    thumb_separador = get_thumb("next.png")
    thumb_settings = get_thumb("setting_0.png")
    
    autoplay.init(item.channel, list_servers, list_quality)
    
    itemlist.append(Item(channel=item.channel, title="Novedades", action="listado", url=host+'torrents', thumbnail=thumb_cartelera, extra="peliculas"))
    itemlist.append(Item(channel=item.channel, title="Por Calidades", action="categorias", url=host, thumbnail=thumb_pelis_hd, extra="peliculas", extra2="categorias"))
    itemlist.append(Item(channel=item.channel, title="Buscar...", action="search", url=host+'buscar?searchword=', thumbnail=thumb_buscar, extra="search"))
    
    itemlist.append(Item(channel=item.channel, url=host, title="[COLOR yellow]Configuración:[/COLOR]", folder=False, thumbnail=thumb_separador))
    
    itemlist.append(Item(channel=item.channel, action="configuracion", title="Configurar canal", thumbnail=thumb_settings))
    
    autoplay.show_option(item.channel, itemlist)            #Activamos Autoplay

    return itemlist
    
    
def configuracion(item):
    from platformcode import platformtools
    ret = platformtools.show_channel_settings()
    platformtools.itemlist_refresh()
    return


def categorias(item):
    logger.info()
    
    itemlist = []
    
    data = ''
    try:
        data = re.sub(r"\n|\r|\t|&nbsp;|<br>|\s{2}|(<!--.*?-->)", "", httptools.downloadpage(item.url, timeout=timeout).data)
        data = unicode(data, "utf-8", errors="replace").encode("utf-8")
    except:
        pass
        
    patron = '<li><a href="([^"]+)" rel="tag" class="[^>]+>(.*?)<\/a><\/li>'
    #Verificamos si se ha cargado una página, y si además tiene la estructura correcta
    if not data or not scrapertools.find_single_match(data, patron):
        item = generictools.web_intervenida(item, data)                         #Verificamos que no haya sido clausurada
        if item.intervencion:                                                   #Sí ha sido clausurada judicialmente
            for clone_inter, autoridad in item.intervencion:
                thumb_intervenido = get_thumb(autoridad)
                itemlist.append(item.clone(action='', title="[COLOR yellow]" + clone_inter.capitalize() + ': [/COLOR]' + intervenido_judicial + '. Reportar el problema en el foro', thumbnail=thumb_intervenido))
            return itemlist                                                     #Salimos
        
        logger.error("ERROR 01: SUBMENU: La Web no responde o ha cambiado de URL: " + item.url)
    if not data:    #Si no ha logrado encontrar nada, salimos
        itemlist.append(item.clone(action='', title=item.category + ': ERROR 01: SUBMENU: La Web no responde o ha cambiado de URL. Si la Web está activa, reportar el error con el log'))
        return itemlist                                 #si no hay más datos, algo no funciona, pintamos lo que tenemos

    matches = re.compile(patron, re.DOTALL).findall(data)

    if not matches:
        logger.error("ERROR 02: SUBMENU: Ha cambiado la estructura de la Web " + " / PATRON: " + patron + " / DATA: " + data)
        itemlist.append(item.clone(action='', title=item.category + ': ERROR 02: SUBMENU: Ha cambiado la estructura de la Web.  Reportar el error con el log'))
        return itemlist                                 #si no hay más datos, algo no funciona, pintamos lo que tenemos

    #logger.debug(matches)

    for scrapedurl, scrapedtitle in matches:

        itemlist.append(item.clone(action="listado", title=scrapedtitle.capitalize().strip(), url=scrapedurl))

    return itemlist
    
    
def listado(item):
    logger.info()
    itemlist = []
    item.category = categoria

    #logger.debug(item)
    
    curr_page = 1                                                               # Página inicial
    cnt_title = 0                                                               # Contador de líneas insertadas en Itemlist
    if item.curr_page:
        curr_page = int(item.curr_page)                                         # Si viene de una pasada anterior, lo usamos
        del item.curr_page                                                      # ... y lo borramos
    if item.last_page:
        last_page = int(item.last_page)                                         # Si viene de una pasada anterior, lo usamos
        del item.last_page                                                      # ... y lo borramos
    
    cnt_tot = 40                                                                # Poner el num. máximo de items por página
    cnt_pct = 0.725                                                             #% de la página a llenar
    inicio = time.time()                                    # Controlaremos que el proceso no exceda de un tiempo razonable
    fin = inicio + 5                                                            # Después de este tiempo pintamos (segundos)
    timeout_search = timeout                                                    # Timeout para descargas
    if item.extra == 'search':
        timeout_search = timeout * 2                                            # Timeout un poco más largo para las búsquedas
        if timeout_search < 5:
            timeout_search = 5                                                  # Timeout un poco más largo para las búsquedas

    if not item.extra2:                                                         # Si viene de Catálogo o de Alfabeto
        item.extra2 = ''
    
    next_page_url = item.url
    #Máximo num. de líneas permitidas por TMDB. Máx de 10 segundos por Itemlist para no degradar el rendimiento
    while cnt_title < cnt_tot * cnt_pct and fin > time.time():
    
        # Descarga la página
        data = ''
        try:
            data = re.sub(r"\n|\r|\t|\s{2}|(<!--.*?-->)|&nbsp;", "", httptools.downloadpage(next_page_url, timeout=timeout_search).data)
            data = unicode(data, "utf-8", errors="replace").encode("utf-8")
        except:
            pass
        
        if not data:                                    #Si la web está caída salimos sin dar error
            logger.error("ERROR 01: LISTADO: La Web no responde o ha cambiado de URL: " + item.url + " / DATA: " + data)
            itemlist.append(item.clone(action='', title=item.channel.capitalize() + ': ERROR 01: LISTADO:.  La Web no responde o ha cambiado de URL. Si la Web está activa, reportar el error con el log'))
            break                                       #si no hay más datos, algo no funciona, pintamos lo que tenemos
        
        #Patrón para todo, menos para Alfabeto
        if item.extra == 'search':
            patron = '<div class="moditemfdb"><a title="([^"]+)"\s+href="([^"]+)"><img.*?class="thumbnailresult" src="([^"]+)"\/><\/a>'
        elif item.extra2 == 'categorias':
            patron = '<div class="blogitem "><a href="([^"]+)".*?src="([^"]+)" alt.*?title="([^"]+)">'
        else:
            patron = '<div class="blogitem "><a title="([^"]+)"\s+href="([^"]+)">.*?src="([^"]+)" onload'
            
        matches = re.compile(patron, re.DOTALL).findall(data)
        if not matches and not 'Total: 0 resultados encontrados' in data:           #error
            item = generictools.web_intervenida(item, data)                         #Verificamos que no haya sido clausurada
            if item.intervencion:                                                   #Sí ha sido clausurada judicialmente
                item, itemlist = generictools.post_tmdb_episodios(item, itemlist)   #Llamamos al método para el pintado del error
                return itemlist                                                     #Salimos
            
            logger.error("ERROR 02: LISTADO: Ha cambiado la estructura de la Web " + " / PATRON: " + patron + " / DATA: " + data)
            itemlist.append(item.clone(action='', title=item.channel.capitalize() + ': ERROR 02: LISTADO: Ha cambiado la estructura de la Web.  Reportar el error con el log'))
            break                                       #si no hay más datos, algo no funciona, pintamos lo que tenemos
        
        #logger.debug("PATRON: " + patron)
        #logger.debug(matches)
        #logger.debug(data)
        
        #Buscamos la url de paginado y la última página
        patron = '<a href="([^"]+=(\d+))" title="Siguiente">Siguiente<\/a>'
        try:
            next_page_url, curr_page = scrapertools.find_single_match(data, patron)
            curr_page = int(curr_page) / len(matches)
        except:                                                         #Si no lo encuentra, lo ponemos a 1
            #logger.error('ERROR 03: LISTADO: Al obtener la paginación: ' + patron + ' / ' + data)
            fin = 0                                                     #Forzamos a salir  del WHILE al final del FOR
            cnt_title = 0                                               #Evitamos pié de página
            curr_page = 1
            next_page_url = item.url
        next_page_url = urlparse.urljoin(host, next_page_url)
        #logger.debug('curr_page: ' + str(curr_page) + ' / url: ' + next_page_url)
        
        #Empezamos el procesado de matches
        for scrapedtitle, scrapedurl, scrapedthumb in matches:
            if item.extra2 == 'categorias':                                 #Cambia el orden de tres parámetros (Categorías)
                title = scrapedthumb
                url = urlparse.urljoin(host, scrapedtitle)
                thumb = scrapedurl
            else:                                                           #lo estándar
                title = scrapedtitle
                url = urlparse.urljoin(host, scrapedurl)
                thumb = scrapedthumb
                

            quality = scrapertools.find_single_match(title, '\[(.*?)\]')    #capturamos quality
            title = re.sub(r'\[.*?\]', '', title)                           #y lo borramos de title

            title = title.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü", "u").replace("ï¿½", "ñ").replace("Ã±", "ñ").replace("&atilde;", "a").replace("&etilde;", "e").replace("&itilde;", "i").replace("&otilde;", "o").replace("&utilde;", "u").replace("&ntilde;", "ñ").replace("&#8217;", "'")

            item_local = item.clone()                                       #Creamos copia de Item para trabajar
            if item_local.tipo:                                             #... y limpiamos
                del item_local.tipo
            if item_local.totalItems:
                del item_local.totalItems
            if item_local.post_num:
                del item_local.post_num
            if item_local.intervencion:
                del item_local.intervencion
            if item_local.viewmode:
                del item_local.viewmode
            item_local.text_bold = True
            del item_local.text_bold
            item_local.text_color = True
            del item_local.text_color
                
            title_subs = []                                                 #creamos una lista para guardar info importante
            item_local.language = []                                        #iniciamos Lenguaje
            item_local.quality = quality                                    #guardamos la calidad, si la hay
            item_local.url = url                                            #guardamos el thumb
            item_local.thumbnail = thumb                                    #guardamos el thumb
            item_local.context = "['buscar_trailer']"
            
            item_local.contentType = "movie"                                #por defecto, son películas
            item_local.action = "findvideos"

            #Ajustamos los idiomas
            if ("-latino-" in url.lower() or "(latino)" in title.lower()) and "LAT" not in item_local.language:
                item_local.language += ['LAT']
            elif ('-vos-' in url.lower() or '-vose-' in url.lower() or '(vos)' in title.lower() or '(vose)' in title.lower()) and "VOSE" not in item_local.language:
                item_local.language += ['VOSE']
            elif ('-vo-' in url.lower() or '(vo)' in title.lower()) and "VO" not in item_local.language:
                item_local.language += ['VO']
            
            if item_local.language == []:
                item_local.language = ['CAST']                              #Por defecto
                
            title = re.sub(r'\(.*?\)', '', title)                           #Limpiamos del idioma de title

            #Detectamos info interesante a guardar para después de TMDB
            if scrapertools.find_single_match(title, '[m|M].*?serie'):
                title = re.sub(r'[m|M]iniserie', '', title)
                title_subs += ["Miniserie"]
            if scrapertools.find_single_match(title, '[s|S]aga'):
                title = re.sub(r'[s|S]aga', '', title)
                title_subs += ["Saga"]
            if scrapertools.find_single_match(title, '[c|C]olecc'):
                title = re.sub(r'[c|C]olecc...', '', title)
                title_subs += ["Colección"]
                
            if "duolog" in title.lower():
                title_subs += ["[Saga]"]
                title = title.replace(" Duologia", "").replace(" duologia", "").replace(" Duolog", "").replace(" duolog", "")
            if "trilog" in title.lower():
                title_subs += ["[Saga]"]
                title = title.replace(" Trilogia", "").replace(" trilogia", "").replace(" Trilog", "").replace(" trilog", "")
            if "extendida" in title.lower() or "v.e." in title.lower()or "v e " in title.lower():
                title_subs += ["[V. Extendida]"]
                title = title.replace("Version Extendida", "").replace("(Version Extendida)", "").replace("V. Extendida", "").replace("VExtendida", "").replace("V Extendida", "").replace("V.Extendida", "").replace("V  Extendida", "").replace("V.E.", "").replace("V E ", "").replace("V:Extendida", "")

            item_local.infoLabels["year"] = '-'                             #Reseteamos el año para TMDB
            
            #Limpiamos el título de la basura innecesaria
            title = re.sub(r'- $', '', title)
            title = re.sub(r'TV|Online|Spanish|Torrent|en Espa\xc3\xb1ol|Español|Latino|Subtitulado|Blurayrip|Bluray rip|\[.*?\]|R2 Pal|\xe3\x80\x90 Descargar Torrent \xe3\x80\x91|Completa|Temporada|Descargar|Torren', '', title, flags=re.IGNORECASE)

            #Terminamos de limpiar el título
            title = re.sub(r'\??\s?\d*?\&.*', '', title)
            title = re.sub(r'[\(|\[]\s+[\)|\]]', '', title)
            title = title.replace('()', '').replace('[]', '').strip().lower().title()
            
            item_local.from_title = title.strip().lower().title()   #Guardamos esta etiqueta para posible desambiguación de título

            #Salvamos el título según el tipo de contenido
            if item_local.contentType == "movie":
                item_local.contentTitle = title.strip().lower().title()
            else:
                item_local.contentSerieName = title.strip().lower().title()

            item_local.title = title.strip().lower().title()            #Guardamos el título
                
            #Guarda la variable temporal que almacena la info adicional del título a ser restaurada después de TMDB
            item_local.title_subs = title_subs

            #Ahora se filtra por idioma, si procede, y se pinta lo que vale
            if config.get_setting('filter_languages', channel) > 0:     #Si hay idioma seleccionado, se filtra
                itemlist = filtertools.get_link(itemlist, item_local, list_language)
            else:
                itemlist.append(item_local.clone())                     #Si no, pintar pantalla
            
            cnt_title = len(itemlist)                                   #Contador de líneas añadidas

            #logger.debug(item_local)

    #Pasamos a TMDB la lista completa Itemlist
    tmdb.set_infoLabels(itemlist, __modo_grafico__)
    
    #Llamamos al método para el maquillaje de los títulos obtenidos desde TMDB
    item, itemlist = generictools.post_tmdb_listado(item, itemlist)

    # Si es necesario añadir paginacion
    if cnt_title >= cnt_tot * cnt_pct:

        title = '%s' % curr_page

        itemlist.append(Item(channel=item.channel, action="listado", title=">> Página siguiente " + title, url=next_page_url, extra=item.extra, extra2=item.extra2))

    return itemlist

    
def findvideos(item):
    logger.info()
    itemlist = []
    itemlist_t = []                                     #Itemlist total de enlaces
    itemlist_f = []                                     #Itemlist de enlaces filtrados
    if not item.language:
        item.language = ['CAST']                        #Castellano por defecto

    item.category = categoria
    
    item.extra2 = 'xyz'
    del item.extra2
    
    #logger.debug(item)

    #Bajamos los datos de la página
    data = ''
    patron = '<p><a href="([^"]+)" rel'
    try:
        data = re.sub(r"\n|\r|\t|\s{2}|(<!--.*?-->)|&nbsp;", "", httptools.downloadpage(item.url, timeout=timeout).data)
        data = unicode(data, "utf-8", errors="replace").encode("utf-8")
    except:
        pass
        
    if not data:
        logger.error("ERROR 01: FINDVIDEOS: La Web no responde o la URL es erronea: " + item.url)
        itemlist.append(item.clone(action='', title=item.channel.capitalize() + ': ERROR 01: FINDVIDEOS:.  La Web no responde o la URL es erronea. Si la Web está activa, reportar el error con el log'))
        return itemlist                                 #si no hay más datos, algo no funciona, pintamos lo que tenemos

    matches = re.compile(patron, re.DOTALL).findall(data)
    if not matches:                                     #error
        logger.error("ERROR 02: FINDVIDEOS: No hay enlaces o ha cambiado la estructura de la Web " + " / PATRON: " + patron + data)
        itemlist.append(item.clone(action='', title=item.channel.capitalize() + ': ERROR 02: FINDVIDEOS: No hay enlaces o ha cambiado la estructura de la Web.  Verificar en la Web esto último y reportar el error con el log'))
        return itemlist                                 #si no hay más datos, algo no funciona, pintamos lo que tenemos
    
    #logger.debug("PATRON: " + patron)
    #logger.debug(matches)
    #logger.debug(data)
    
    #Llamamos al método para crear el título general del vídeo, con toda la información obtenida de TMDB
    item, itemlist = generictools.post_tmdb_findvideos(item, itemlist)

    #Ahora tratamos los enlaces .torrent
    for scrapedurl in matches:                                          #leemos los torrents con la diferentes calidades
        if 'javascript' in scrapedurl:                                  #evitamos la basura
            continue
        
        url = urlparse.urljoin(host, scrapedurl)
        #Leemos la siguiente página, que es de verdad donde está el magnet/torrent
        try:
            data = re.sub(r"\n|\r|\t|\s{2}|(<!--.*?-->)|&nbsp;", "", httptools.downloadpage(url, timeout=timeout).data)
            data = unicode(data, "utf-8", errors="replace").encode("utf-8")
        except:
            pass
        
        patron = "window.open\('([^']+)'"
        url = scrapertools.find_single_match(data, patron)
        if not url:                                         #error
            logger.error("ERROR 02: FINDVIDEOS: No hay enlaces o ha cambiado la estructura de la Web " + " / PATRON: " + patron + data)
            itemlist.append(item.clone(action='', title=item.channel.capitalize() + ': ERROR 02: FINDVIDEOS: No hay enlaces o ha cambiado la estructura de la Web.  Verificar en la Web esto último y reportar el error con el log'))
            continue                                        #si no hay más datos, algo no funciona, pasamos al siguiente
        
        #Generamos una copia de Item para trabajar sobre ella
        item_local = item.clone()
            
        item_local.url = urlparse.urljoin(host, url)
        
        #Buscamos si ya tiene tamaño, si no, los buscamos en el archivo .torrent
        size = scrapertools.find_single_match(item_local.quality, '\s\[(\d+,?\d*?\s\w\s?[b|B])\]')
        if not size:
            size = generictools.get_torrent_size(item_local.url)                #Buscamos el tamaño en el .torrent
        if size:
            item_local.title = re.sub(r'\s\[\d+,?\d*?\s\w[b|B]\]', '', item_local.title) #Quitamos size de título, si lo traía
            item_local.title = '%s [%s]' % (item_local.title, size)             #Agregamos size al final del título
            size = size.replace('GB', 'G B').replace('Gb', 'G b').replace('MB', 'M B').replace('Mb', 'M b')
        item_local.quality = re.sub(r'\s\[\d+,?\d*?\s\w\s?[b|B]\]', '', item_local.quality)    #Quitamos size de calidad, si lo traía
        item_local.quality = '%s [%s]' % (item_local.quality, size)             #Agregamos size al final de la calidad
        
        #Ahora pintamos el link del Torrent
        item_local.title = '[COLOR yellow][?][/COLOR] [COLOR yellow][Torrent][/COLOR] [COLOR limegreen][%s][/COLOR] [COLOR red]%s[/COLOR]' % (item_local.quality, str(item_local.language))
        
        #Preparamos título y calidad, quitamos etiquetas vacías
        item_local.title = re.sub(r'\s?\[COLOR \w+\]\[\[?\s?\]?\]\[\/COLOR\]', '', item_local.title)    
        item_local.title = re.sub(r'\s?\[COLOR \w+\]\s?\[\/COLOR\]', '', item_local.title)
        item_local.title = item_local.title.replace("--", "").replace("[]", "").replace("()", "").replace("(/)", "").replace("[/]", "").strip()
        item_local.quality = re.sub(r'\s?\[COLOR \w+\]\[\[?\s?\]?\]\[\/COLOR\]', '', item_local.quality)
        item_local.quality = re.sub(r'\s?\[COLOR \w+\]\s?\[\/COLOR\]', '', item_local.quality).strip()
        item_local.quality = item_local.quality.replace("--", "").replace("[]", "").replace("()", "").replace("(/)", "").replace("[/]", "").strip()

        item_local.alive = "??"                                                 #Calidad del link sin verificar
        item_local.action = "play"                                              #Visualizar vídeo
        item_local.server = "torrent"                                           #Servidor Torrent
        
        itemlist_t.append(item_local.clone())                                   #Pintar pantalla, si no se filtran idiomas
        
        # Requerido para FilterTools
        if config.get_setting('filter_languages', channel) > 0:                 #Si hay idioma seleccionado, se filtra
            itemlist_f = filtertools.get_link(itemlist_f, item_local, list_language)  #Pintar pantalla, si no está vacío

        #logger.debug("TORRENT: " + scrapedurl + " / title gen/torr: " + item.title + " / " + item_local.title + " / calidad: " + item_local.quality + " / content: " + item_local.contentTitle + " / " + item_local.contentSerieName)
        
        #logger.debug(item_local)
        
    if len(itemlist_f) > 0:                                                     #Si hay entradas filtradas...
        itemlist.extend(itemlist_f)                                             #Pintamos pantalla filtrada
    else:                                                                       
        if config.get_setting('filter_languages', channel) > 0 and len(itemlist_t) > 0: #Si no hay entradas filtradas ...
            thumb_separador = get_thumb("next.png")                             #... pintamos todo con aviso
            itemlist.append(Item(channel=item.channel, url=host, title="[COLOR red][B]NO hay elementos con el idioma seleccionado[/B][/COLOR]", thumbnail=thumb_separador))
        itemlist.extend(itemlist_t)                                             #Pintar pantalla con todo si no hay filtrado

    # Requerido para AutoPlay
    autoplay.start(itemlist, item)                                              #Lanzamos Autoplay
    
    return itemlist


def actualizar_titulos(item):
    logger.info()
    
    item = generictools.update_title(item) #Llamamos al método que actualiza el título con tmdb.find_and_set_infoLabels
    
    #Volvemos a la siguiente acción en el canal
    return item

    
def search(item, texto):
    logger.info()
    texto = texto.replace(" ", "+")
    
    try:
        item.url = item.url + texto

        if texto != '':
            return listado(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []
 
 
def newest(categoria):
    logger.info()
    itemlist = []
    item = Item()
    
    try:
        if categoria in ['torrent', 'peliculas']:
            item.url = host + 'torrents'
        elif categoria == '4k':
            item.url = host + 'tags/4k'
            item.extra2 = 'categorias'
        item.extra = "peliculas"
        item.channel = channel
        item.category_new= 'newest'

        itemlist = listado(item)
        if ">> Página siguiente" in itemlist[-1].title:
            itemlist.pop()

    # Se captura la excepción, para no interrumpir al canal novedades si un canal falla
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist