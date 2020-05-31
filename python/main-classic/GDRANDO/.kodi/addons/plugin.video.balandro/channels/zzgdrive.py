# -*- coding: utf-8 -*-

import re, os, time, urllib

from platformcode import config, logger
from core.item import Item
from core import httptools, scrapertools, tmdb, servertools

from lib.gdrivetools import gdrive

# Requiere haber añadido manualmente estas claves en settings.xml (copiarlas del settings.xml del addon gdrive abiendo hecho el enroll)
# ~ <setting id="gdrive1_client_id">...</setting>
# ~ <setting id="gdrive1_client_secret">...</setting>
# ~ <setting id="gdrive1_code">...</setting>
# ~ <setting id="gdrive1_username">...</setting>
# ~ <setting id="gdrive1_auth_access_token">...</setting>
# ~ <setting id="gdrive1_auth_refresh_token">...</setting>

perpage = 10 # películas por página (menos de 40 por la limitación de llamadas a tmdb)


def mainlist(item):
    return mainlist_pelis(item)

def mainlist_pelis(item):
    logger.info()
    itemlist = []
    
    gd = gdrive('gdrive1')
    drives = gd.getTeamDrives()
    if not drives:
        platformtools.dialog_notification('Acceso a GDrive', 'Falla el login!')
        return itemlist
    
    for drive_id, drive_name in drives:
        itemlist.append(item.clone( title = drive_name, action = 'list_drive', drive_id = drive_id, drive_name = drive_name ))

    return itemlist



def list_drive(item):
    logger.info()
    itemlist = []

    item.category = item.drive_name

    itemlist.append(item.clone( title = 'Últimos vídeos', action = 'list_all', drive_q = "", nextPageToken=None ))

    itemlist.append(item.clone( title = 'Películas 2020', action = 'list_all', drive_q = "name+contains+'(2020)'", nextPageToken=None ))
    itemlist.append(item.clone( title = 'Películas 2019', action = 'list_all', drive_q = "name+contains+'(2019)'", nextPageToken=None ))
    itemlist.append(item.clone( title = 'Por años', action = 'anios' ))

    itemlist.append(item.clone( title = 'Por generos', action = 'generos' ))

    itemlist.append(item.clone( title = 'Por carpetas', action = 'carpetas', drive_parent = '' ))

    itemlist.append(item.clone( title = 'Buscar vídeo ...', action = 'search', search_type = 'movie' ))
    itemlist.append(item.clone( title = 'Buscar serie ...', action = 'search', search_type = 'tvshow' ))


    itemlist.append(item.clone( title = 'Series', action = 'carpeta_series', drive_parent = "1kBkzN3gpz4te1qpbqZFha_LwvhP3a6-4" ))
    itemlist.append(item.clone( title = 'Series Infantiles', action = 'carpeta_series', drive_parent = "1EJ8aSCS6GO_Y3ueWhDa8cOUndRH7iihL" ))

    itemlist.append(item.clone( title = '3D', action = 'carpetas', drive_parent = "1HEbOPEZjTvZ1N_QmYiHaMcokeQzqd23m" ))
    itemlist.append(item.clone( title = '4K', action = 'carpetas', drive_parent = "1Bms4hlLmEdAQilUw8RY42HY43EiDvtB4" ))

    itemlist.append(item.clone( title = 'Anime', action = 'carpetas', drive_parent = "1rQQSpZo-WXY9UU1IIoxBqUcGBEbVTPxt" ))
    itemlist.append(item.clone( title = 'Documentales', action = 'carpetas', drive_parent = "1rkVSwrdAowfin-8bGREcDqfTPcKPhrRZ" ))
    itemlist.append(item.clone( title = 'Infantil', action = 'carpetas', drive_parent = "1UvmEGTVeXQXZkk0biANZy_1lIXE2BFDY" ))
    itemlist.append(item.clone( title = 'Peliculas', action = 'carpetas', drive_parent = "1sVT3qPAmY58O2OoIEIcjzNa3PwWn1tun" ))
    return itemlist



def anios(item):
    logger.info()
    itemlist = []

    from datetime import datetime
    current_year = int(datetime.today().year)

    for x in range(current_year, 1950, -1):
        itemlist.append(item.clone( title=str(x), action='list_all', drive_q = "name+contains+'(%s)'" % x, nextPageToken=None ))

    return itemlist

def generos(item):
    logger.info()
    itemlist = []

    opciones = ['Acción', 'Animación', 'Aventura', 'Bélica', 'Ciencia ficción', 'Comedia', 'Crimen', 'Drama', 'Familia', 'Fantasía', 'Historia', 'Misterio', 'Música', 'Romance', 'Suspense', 'Terror']
    for x in opciones:
        itemlist.append(item.clone( title=x, action='list_all', drive_q = "name+contains+'(%s)'" % urllib.quote_plus(x) ))

    return itemlist


def carpetas(item):
    logger.info()
    itemlist = []

    if item.drive_parent: q_folder = "'"+str(item.drive_parent)+"'+in+parents"
    else: q_folder = "'"+str(item.drive_id)+"'+in+parents"

    q = "mimeType+=+'application/vnd.google-apps.folder'+and+trashed%3Dfalse+and+" + q_folder

    gd = gdrive('gdrive1')
    files = gd.getFiles(item.drive_id, q=q, nextPageToken=item.nextPageToken, perpage=50, orden='name')
    
    if files and 'files' in files:
        for f in files['files']:
            itemlist.append(item.clone( title=f['name'], action='carpetas', drive_parent = f['id'], nextPageToken=None ))
            logger.info('%s %s' % (f['id'], f['name']))

    if 'nextPageToken' in files and files['nextPageToken']:
        itemlist.append(item.clone( title=">> Siguientes carpetas", nextPageToken=files['nextPageToken'], action='carpetas' ))

    # ~ if len(itemlist) == 0: # Si no hay subcarpetas, listar si tiene vídeos
        # ~ return list_all(item)
    itemlist.extend(list_all(item)) # listar siempre ambas

    return itemlist


def carpeta_series(item):
    logger.info()
    itemlist = []

    if item.drive_parent: q_folder = "'"+str(item.drive_parent)+"'+in+parents"
    else: q_folder = "'"+str(item.drive_id)+"'+in+parents"

    q = "mimeType+=+'application/vnd.google-apps.folder'+and+trashed%3Dfalse+and+" + q_folder

    gd = gdrive('gdrive1')
    files = gd.getFiles(item.drive_id, q=q, nextPageToken=item.nextPageToken, perpage=10, orden='name')
    
    if files and 'files' in files:
        for f in files['files']:
            title = f['name']
            year = scrapertools.find_single_match(title, '\((\d{4})\)')
            if year:
                title = title.replace('(%s)' % year, '').strip()
            else:
                year = '-'

            itemlist.append(item.clone( action='carpeta_temporadas', title=title, drive_parent=f['id'], nextPageToken=None,
                                        thumbnail=config.get_thumb('dev'),
                                        contentType='tvshow', contentSerieName=title, infoLabels={'year': year, 'tvshowtitle': title} ))

    tmdb.set_infoLabels(itemlist)

    if 'nextPageToken' in files and files['nextPageToken']:
        itemlist.append(item.clone( title=">> Página siguiente", nextPageToken=files['nextPageToken'], action='carpeta_series' ))

    return itemlist

def carpeta_temporadas(item):
    logger.info()
    itemlist = []

    if item.drive_parent: q_folder = "'"+str(item.drive_parent)+"'+in+parents"
    else: q_folder = "'"+str(item.drive_id)+"'+in+parents"

    q = "mimeType+=+'application/vnd.google-apps.folder'+and+trashed%3Dfalse+and+" + q_folder

    gd = gdrive('gdrive1')
    files = gd.getFiles(item.drive_id, q=q, perpage=20, orden='name')
    
    if files and 'files' in files:
        for f in files['files']:
            season = scrapertools.find_single_match(f['name'], '(\d+)')

            itemlist.append(item.clone( action='list_all', title=f['name'], drive_parent=f['id'],
                                        thumbnail=config.get_thumb('dev'),
                                        contentType='season', contentSeason = season ))
            
    tmdb.set_infoLabels(itemlist)

    return itemlist



def list_all(item):
    logger.info()
    itemlist = []
    
    q = "mimeType+contains+'video'+and+trashed%3Dfalse"
    if item.drive_q: q += "+and+" + item.drive_q
    if item.drive_parent: q += "+and+" + "'"+str(item.drive_parent)+"'+in+parents"
    # ~ else: q += "+and+" + "not+'1ovn8Mslg4A5cwaPv-DLmA40SFxgzx0Pg'+in+parents" # descartar de Subidas !?

    orden = 'name' if item.drive_parent else 'modifiedTime+desc'

    gd = gdrive('gdrive1')
    files = gd.getFiles(item.drive_id, q=q, nextPageToken=item.nextPageToken, perpage=perpage, orden=orden)
    
    if not files or 'files' not in files: return itemlist
    
    for f in files['files']:
        
        title = f['name']

        title = title.replace('.mkv','').replace('.avi','').replace('.mp4','') #TODO otras extensiones ?

        tipo = 'movie'
        year = scrapertools.find_single_match(title, '\((\d{4})\)')
        if year:
            aux = title.split('(%s)' % year)
            title = aux[0].strip()
            info = aux[1].replace('...','').strip()
            titulo = '%s [COLOR red]%s[/COLOR]' % (title, info)
            title = title.replace('Copia de ', '')
        else:
            year = '-'
            titulo = title
            s_e = scrapertools.find_single_match(title, '(?i) - S(\d+)E(\d+) -')
            if s_e:
                tipo = 'tvshow'
                title = title.split(' - ')[0].strip()
                season = s_e[0]
                episode = s_e[1]

        if tipo == 'movie':
            itemlist.append(item.clone( action='findvideos', title=titulo, file_id=f['id'],
                                        thumbnail=config.get_thumb('dev'),
                                        contentType='movie', contentTitle=title, infoLabels={'year': year} ))
        else:
            if item.contentSerieName:
                itemlist.append(item.clone( action='findvideos', title=titulo, file_id=f['id'],
                                            thumbnail=config.get_thumb('dev'),
                                            contentType='episode', contentSeason = season, contentEpisodeNumber = episode ))
            else:
                itemlist.append(item.clone( action='findvideos', title=titulo, file_id=f['id'],
                                            thumbnail=config.get_thumb('dev'),
                                            contentType='episode', contentSerieName=title, contentSeason = season, contentEpisodeNumber = episode ))

    tmdb.set_infoLabels(itemlist)

    if 'nextPageToken' in files and files['nextPageToken']:
        itemlist.append(item.clone( title=">> Página siguiente", nextPageToken=files['nextPageToken'], action='list_all' ))
        
    return itemlist


def findvideos(item):
    logger.info()
    itemlist = []
    
    gd = gdrive('gdrive1')

    datos = gd.getFileInfo(item.file_id)
    if datos and 'url_directo' in datos:
        try:
            qlty = '%sx%s' % (datos['videoMediaMetadata']['width'], datos['videoMediaMetadata']['height'])
        except:
            qlty = 'Original'
        try:
            othr = ''
            othr = config.format_bytes(int(datos['size']))
            othr += ', %s' % config.format_seconds_to_duration(int(datos['videoMediaMetadata']['durationMillis'])/1000)
        except:
            pass
        itemlist.append(Item( channel = item.channel, action = 'play', server = 'directo', title = '', url = datos['url_directo'], quality = qlty, other=othr ))
    
        if datos['extra']:
            for v in datos['extra']:
                itemlist.append(Item( channel = item.channel, action = 'play', server = 'directo', title = '', url = v[1], quality = v[0] ))

    return itemlist



def search_series(item):
    logger.info()
    itemlist = []

    q_folder = "('1kBkzN3gpz4te1qpbqZFha_LwvhP3a6-4'+in+parents"
    q_folder += "+or+'1EJ8aSCS6GO_Y3ueWhDa8cOUndRH7iihL'+in+parents)"
    if item.drive_q: q_folder += "+and+" + item.drive_q

    q = "mimeType+=+'application/vnd.google-apps.folder'+and+trashed%3Dfalse+and+" + q_folder

    gd = gdrive('gdrive1')
    files = gd.getFiles(item.drive_id, q=q, nextPageToken=item.nextPageToken, perpage=10, orden='name')
    
    if files and 'files' in files:
        for f in files['files']:
            title = f['name']
            year = scrapertools.find_single_match(title, '\((\d{4})\)')
            if year:
                title = title.replace('(%s)' % year, '').strip()
            else:
                year = '-'

            itemlist.append(item.clone( action='carpeta_temporadas', title=title, drive_parent=f['id'], nextPageToken=None,
                                        thumbnail=config.get_thumb('dev'),
                                        contentType='tvshow', contentSerieName=title, infoLabels={'year': year, 'tvshowtitle': title} ))

    tmdb.set_infoLabels(itemlist)

    if 'nextPageToken' in files and files['nextPageToken']:
        itemlist.append(item.clone( title=">> Página siguiente", nextPageToken=files['nextPageToken'], action='search_series' ))

    return itemlist


def search(item, texto):
    logger.info()
    try:
        if not item.drive_id: return []
        item.drive_q = "name+contains+'%s'" % urllib.quote_plus(texto.replace("'",''))
        item.nextPageToken = None
        if item.search_type == 'tvshow':
            return search_series(item)
        else:
            return list_all(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []
